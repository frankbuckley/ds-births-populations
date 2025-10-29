"""Combine Parquet files."""

import pathlib
import polars as pl


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_parquet = src_dir / "us_births.parquet"  # destination

    out_parquet.unlink(missing_ok=True)

    paths = list(src_dir.glob("*.parquet"))
    paths.sort(reverse=True)
    
    if not paths:
        raise FileNotFoundError(f"No input Parquet files found in {src_dir.resolve()}")

    lfs = [pl.scan_parquet(p) for p in paths]

    combined = pl.concat(lfs, how="diagonal_relaxed")

    combined.sink_parquet(out_parquet.as_posix())

    print(f"Wrote: {out_parquet}")


if __name__ == "__main__":
    combine_all()
