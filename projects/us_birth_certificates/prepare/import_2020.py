"""Reads selected columns from 2020 data file and saves to Parquet file."""

import pandas as pd

from . import colspecs
from . import columns


def import_2020() -> pd.DataFrame:
    "Reads selected columns from 2020 data file and saves to Parquet file."

    print("Importing 2020 data...")

    df = pd.read_fwf(
        "data/Nat2020us/Nat2020PublicUS.c20210506.r20210812.txt",
        colspecs=colspecs.colspecs_2020,
        header=None,
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2020"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Adding computed columns...")

    df = columns.add_computed_columns(df)

    print("Saving to data/us_births_2020.parquet...")

    df.to_parquet("data/us_births_2020.parquet")

    return df


if __name__ == "__main__":
    import_2020()
