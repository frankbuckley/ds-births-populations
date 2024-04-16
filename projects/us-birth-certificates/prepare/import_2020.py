"""Reads selected columns from 2020 data file and saves to Parquet file."""

import pandas as pd

import colspecs
import columns


def import_2020():
    "Reads selected columns from 2020 data file and saves to Parquet file."

    print("Importing 2020 data...")

    df = pd.read_fwf(
        "data/Nat2020us/Nat2020PublicUS.c20210506.r20210812.txt",
        colspecs=colspecs.colspecs_2020,
        header=None,
        dtype_backend="pyarrow",
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2020"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Saving to data/us_births_2020.parquet...")

    df.to_parquet("data/us_births_2020.parquet")


if __name__ == "__main__":
    import_2020()
