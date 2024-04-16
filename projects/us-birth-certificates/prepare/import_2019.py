"""Reads selected columns from 2019 data file and saves to Parquet file."""

import pandas as pd

import colspecs
import columns


def import_2019():
    "Reads selected columns from 2019 data file and saves to Parquet file."

    print("Importing 2019 data...")

    df = pd.read_fwf(
        "data/Nat2019us/Nat2019PublicUS.c20200506.r20200915.txt",
        colspecs=colspecs.colspecs_2019,
        header=None,
        dtype_backend="pyarrow",
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2019"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Saving to data/us_births_2019.parquet...")

    df.to_parquet("data/us_births_2019.parquet")


if __name__ == "__main__":
    import_2019()
