"""Reads selected columns from 2018 data file and saves to Parquet file."""

import pandas as pd

from . import colspecs
from . import columns

def import_2018() -> pd.DataFrame:
    "Reads selected columns from 2018 data file and saves to Parquet file."

    print("Importing 2018 data...")

    df = pd.read_fwf(
        "data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt",
        colspecs=colspecs.colspecs_2018,
        header=None,
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2018"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Adding computed columns...")

    df = columns.add_computed_columns(df)

    print("Saving to data/us_births_2018.parquet...")

    df.to_parquet("data/us_births_2018.parquet")

    return df


if __name__ == "__main__":
    import_2018()
