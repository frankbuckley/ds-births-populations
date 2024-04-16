"""Reads selected columns from 2022 data file and saves to Parquet file."""

import pandas as pd

import colspecs
import columns


def import_2022():
    "Reads selected columns from 2022 data file and saves to Parquet file."

    print("Importing 2022 data...")

    df = pd.read_fwf(
        "data/Nat2022us/Nat2022PublicUS.c20230504.r20230822.txt",
        colspecs=colspecs.colspecs_2022,
        header=None,
        dtype_backend="pyarrow",
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2022"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Saving to data/us_births_2022.parquet...")

    df.to_parquet("data/us_births_2022.parquet")


if __name__ == "__main__":
    import_2022()
