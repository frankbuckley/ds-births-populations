"""Combines Parquet files to single Parquet file."""

import duckdb
import pathlib
import pandas as pd

PARQUET_ENGINE = "fastparquet"


def combine_all():
    "Combines Parquet files to single DataFrame and saves as Parquet file."

    files = pathlib.Path("data").glob("*.parquet")

    to_read = []

    for file in files:
        if (
            any(char.isdigit() for char in file.stem)
            and sum(c.isdigit() for c in file.stem) >= 4
        ):
            to_read.append(file)

    to_read.sort(reverse=True)

    parquet_path = pathlib.Path("data/us_births.parquet")
    if parquet_path.exists():
        parquet_path.unlink()

    db_path = pathlib.Path("data/us_births.db")
    if db_path.exists():
        db_path.unlink()

    combined = pd.DataFrame()

    for file in to_read:
        print(f"Processing {file}")
        df = pd.read_parquet(file, engine=PARQUET_ENGINE)
        combined = pd.concat([combined, df], ignore_index=True)

    combined = combined.reset_index(drop=True)

    combined.to_parquet(parquet_path, engine=PARQUET_ENGINE)

    con = duckdb.connect(db_path)

    con.sql("CREATE TABLE us_births AS SELECT * FROM combined")

    con.close()


if __name__ == "__main__":
    combine_all()
