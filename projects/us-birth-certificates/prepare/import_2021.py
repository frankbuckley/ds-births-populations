"""Reads selected columns from 2021 data file and saves to Parquet file."""

import pandas as pd

import colspecs
import columns


def import_2021() -> pd.DataFrame:
    "Reads selected columns from 2021 data file and saves to Parquet file."

    print("Importing 2021 data...")

    df = pd.read_fwf(
        "data/Nat2021us/Nat2021US.txt",
        colspecs=colspecs.colspecs_2021,
        header=None,
        dtype_backend="pyarrow",
    ).convert_dtypes()

    df.attrs["description"] = "US Births 2021"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Saving to data/us_births_2021.parquet...")

    df.to_parquet("data/us_births_2021.parquet")

    return df


if __name__ == "__main__":
    import_2021()
