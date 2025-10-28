"""Combine Parquet files → one Parquet → DuckDB table, with schema alignment."""

from __future__ import annotations

import pathlib
import polars as pl
import duckdb
from typing import Iterable, Dict


def list_input_parquet(
    src_dir: pathlib.Path, exclude: pathlib.Path
) -> list[pathlib.Path]:
    """List .parquet under src_dir, excluding the destination file if present."""
    files = sorted(src_dir.glob("*.parquet"))
    return [p for p in files if p.resolve() != exclude.resolve()]


def choose_target_dtype(dtypes: Iterable[pl.DataType]) -> pl.DataType:
    """
    Pick a unified dtype for one column across inputs.
    - If all equal: return that.
    - If mixed numerics: Float64.
    - Else: Utf8 (string) for safety.
    """
    dts = list(
        {str(dt) for dt in dtypes}
    )  # compare by string repr to avoid identity issues
    if len(dts) == 1:
        # Parse back to a Polars dtype object
        return next(iter(dtypes))

    # Check if all are numeric
    def is_numeric(dt: pl.DataType) -> bool:
        return pl.datatypes.is_numeric_dtype(dt)

    if all(is_numeric(dt) for dt in dtypes):
        return pl.Float64

    # Fallback
    return pl.Utf8


def build_target_schema(lfs: list[pl.LazyFrame]) -> Dict[str, pl.DataType]:
    """
    Union all column names; pick a target dtype per column using the rule above.
    """
    # Collect schemas from lazy sources (no data read)
    schemas = [lf.schema for lf in lfs]

    # Union of names
    all_names: set[str] = set().union(*(sch.keys() for sch in schemas))

    # For each name, gather dtypes found across inputs
    name_to_dtypes: dict[str, list[pl.DataType]] = {name: [] for name in all_names}
    for sch in schemas:
        for name in all_names:
            dt = sch.get(name)
            if dt is not None:
                name_to_dtypes[name].append(dt)

    # Decide target dtype per column
    target: Dict[str, pl.DataType] = {}
    for name, dts in name_to_dtypes.items():
        target[name] = choose_target_dtype(dts) if dts else pl.Null

    return target


def align_lazyframe(
    lf: pl.LazyFrame, target_schema: Dict[str, pl.DataType]
) -> pl.LazyFrame:
    """
    Ensure lf has exactly the columns and dtypes of target_schema.
    - Add missing columns as nulls with target dtype.
    - Cast existing columns to the target dtype.
    - Reorder columns deterministically.
    """
    present = set(lf.schema.keys())
    want_names = list(sorted(target_schema.keys()))  # stable order

    # Add missing as nulls with desired dtype
    missing_exprs = [
        pl.lit(None, dtype=target_schema[name]).alias(name)
        for name in (present ^ set(want_names))
        if name not in present
    ]

    # Cast existing to desired dtype
    cast_exprs = [
        pl.col(name).cast(target_schema[name]).alias(name)
        for name in (present & set(want_names))
    ]

    lf2 = lf.with_columns(missing_exprs + cast_exprs).select(want_names)
    return lf2


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_parquet = src_dir / "us_births.parquet"  # destination
    out_db = src_dir / "us_births.db"

    # Remove previous outputs to avoid including them as inputs
    out_parquet.unlink(missing_ok=True)
    out_db.unlink(missing_ok=True)

    # Discover inputs and exclude destination
    paths = list_input_parquet(src_dir, exclude=out_parquet)
    if not paths:
        raise FileNotFoundError(f"No input Parquet files found in {src_dir.resolve()}")

    # Build lazy scans
    lfs = [pl.scan_parquet(p) for p in paths]

    # Create a unified target schema from the discovered inputs
    target_schema = build_target_schema(lfs)

    # Align every lazyframe to the target schema
    aligned = [align_lazyframe(lf, target_schema) for lf in lfs]

    # Now concat strictly (schemas already aligned)
    combined = pl.concat(aligned, how="vertical")

    # Stream to Parquet
    combined.sink_parquet(out_parquet.as_posix())

    # Create DuckDB table from the written Parquet
    con = duckdb.connect(out_db.as_posix())
    try:
        con.execute(
            """
            CREATE TABLE us_births AS
            SELECT * FROM read_parquet(?)
        """,
            [out_parquet.as_posix()],
        )
    finally:
        con.close()

    print(f"Wrote: {out_parquet}")
    print(f"DuckDB table created at: {out_db}")


if __name__ == "__main__":
    combine_all()
