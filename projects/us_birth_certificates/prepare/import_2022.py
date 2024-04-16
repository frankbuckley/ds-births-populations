"""Reads selected columns from 2022 data file and saves to Parquet file."""

import pandas as pd

from . import colspecs
from . import columns


def import_2022() -> pd.DataFrame:
    "Reads selected columns from 2022 data file and saves to Parquet file."

    print("Importing 2022 data...")

    df = pd.read_fwf(
        "data/Nat2022us/Nat2022PublicUS.c20230504.r20230822.txt",
        colspecs=colspecs.colspecs_2022,
        header=None,
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2022"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Adding computed columns...")

    df = columns.add_computed_columns(df)

    print("Saving to data/us_births_2022.parquet...")

    df.to_parquet("data/us_births_2022.parquet")

    return df


if __name__ == "__main__":
    import_2022()
