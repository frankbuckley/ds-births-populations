"""Combine Parquet files → one Parquet → DuckDB table, with schema alignment."""

import pathlib
import duckdb


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_parquet = src_dir / "us_births.parquet"
    out_db = src_dir / "us_births.db"

    out_db.unlink(missing_ok=True)

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

    print(f"DuckDB table created at: {out_db}")


if __name__ == "__main__":
    combine_all()
