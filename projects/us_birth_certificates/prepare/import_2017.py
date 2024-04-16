"""Reads selected columns from 2017 data file and saves to Parquet file."""

import pandas as pd

from . import colspecs
from . import columns


def import_2017() -> pd.DataFrame:
    "Reads selected columns from 2017 data file and saves to Parquet file."

    print("Importing 2017 data...")

    df = pd.read_fwf(
        "data/Nat2017us/Nat2017PublicUS.c20180516.r20180808.txt",
        colspecs=colspecs.colspecs_2017,
        header=None,
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2017"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Adding computed columns...")

    df = columns.add_computed_columns(df)

    print("Saving to data/us_births_2017.parquet...")

    df.to_parquet("data/us_births_2017.parquet")

    return df


if __name__ == "__main__":
    import_2017()
