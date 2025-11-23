"""
Create DuckDB database from combined Parquet file.
"""
import pathlib
import duckdb


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    source_parquet = src_dir / "us_births_combined.parquet"
    out_db_temp = src_dir / "us_births_temp.db"
    out_db_temp.unlink(missing_ok=True)

    con = duckdb.connect(out_db_temp.as_posix())

    print("--------------------------------------------------------------")
    print(f"Importing Parquet file into DuckDB '{out_db_temp}'...")
    print("--------------------------------------------------------------")

    try:
        print(f"Reading Parquet file '{source_parquet}'...")

        con.execute(
            """
            CREATE TABLE us_births AS
            SELECT *
            FROM read_parquet(?)
            """,
            [source_parquet.as_posix()],
        )

    finally:
        con.close()


if __name__ == "__main__":
    combine_all()
