"""Reads selected columns from data files and saves to Parquet files."""


import pandas as pd

from . import colspecs
from . import columns


def import_all():
    "Reads selected columns from all data files and saves to Parquet files."

    data_2014 = import_2014()
    data_2015 = import_2015()
    data_2016 = import_2016()
    data_2017 = import_2017()
    data_2018 = import_2018()
    data_2019 = import_2019()
    data_2020 = import_2020()
    data_2021 = import_2021()
    data_2022 = import_2022()

    data_all = pd.concat(
        [data_2014, data_2015, data_2016, data_2017, data_2018, data_2019, data_2020,
            data_2021, data_2022], ignore_index=True
    )

    data_all.to_parquet("data/us_births_all.parquet")


def prepare_import(df: pd.DataFrame, year: int) -> pd.DataFrame:
    "Configures the columns in the data file and saves to Parquet file."

    df.attrs["description"] = f"US Births {year}"

    print("Renaming columns...")

    columns.rename_columns(df)

    print("Setting column types...")

    df = columns.set_column_types(df)

    print("Adding computed columns...")

    df = columns.add_computed_columns(df)

    print(f"Saving to data/us_births_{year}.parquet...")

    df.to_parquet(f"data/us_births_{year}.parquet")

    return df


def import_2014() -> pd.DataFrame:
    "Reads selected columns from 2014 data file and saves to Parquet file."

    print("Importing 2014 data...")

    df = pd.read_fwf(
        "data/Nat2014us/Nat2014PublicUS.c20150514.r20151022.txt",
        colspecs=colspecs.colspecs_2014,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2014)

    return df


def import_2015() -> pd.DataFrame:
    "Reads selected columns from 2015 data file and saves to Parquet file."

    print("Importing 2015 data...")

    df = pd.read_fwf(
        "data/Nat2015us/Nat2015PublicUS.c20160517.r20160907.txt",
        colspecs=colspecs.colspecs_2015,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2015)

    return df


def import_2016() -> pd.DataFrame:
    "Reads selected columns from 2016 data file and saves to Parquet file."

    print("Importing 2016 data...")

    df = pd.read_fwf(
        "data/Nat2016us/Nat2016PublicUS.c20170517.r20190620.txt",
        colspecs=colspecs.colspecs_2016,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2016)

    return df


def import_2017() -> pd.DataFrame:
    "Reads selected columns from 2017 data file and saves to Parquet file."

    print("Importing 2017 data...")

    df = pd.read_fwf(
        "data/Nat2017us/Nat2017PublicUS.c20180516.r20180808.txt",
        colspecs=colspecs.colspecs_2017,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2017)

    return df


def import_2018() -> pd.DataFrame:
    "Reads selected columns from 2018 data file and saves to Parquet file."

    print("Importing 2018 data...")

    df = pd.read_fwf(
        "data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt",
        colspecs=colspecs.colspecs_2018,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2018)

    return df


def import_2019() -> pd.DataFrame:
    "Reads selected columns from 2019 data file and saves to Parquet file."

    print("Importing 2019 data...")

    df = pd.read_fwf(
        "data/Nat2019us/Nat2019PublicUS.c20200506.r20200915.txt",
        colspecs=colspecs.colspecs_2019,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2019)

    return df


def import_2020() -> pd.DataFrame:
    "Reads selected columns from 2020 data file and saves to Parquet file."

    print("Importing 2020 data...")

    df = pd.read_fwf(
        "data/Nat2020us/Nat2020PublicUS.c20210506.r20210812.txt",
        colspecs=colspecs.colspecs_2020,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2020)

    return df


def import_2021() -> pd.DataFrame:
    "Reads selected columns from 2021 data file and saves to Parquet file."

    print("Importing 2021 data...")

    df = pd.read_fwf(
        "data/Nat2021us/Nat2021US.txt",
        colspecs=colspecs.colspecs_2021,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2021)

    return df


def import_2022() -> pd.DataFrame:
    "Reads selected columns from 2022 data file and saves to Parquet file."

    print("Importing 2022 data...")

    df = pd.read_fwf(
        "data/Nat2022us/Nat2022PublicUS.c20230504.r20230822.txt",
        colspecs=colspecs.colspecs_2022,
        header=None,
    ).convert_dtypes()

    prepare_import(df, 2022)

    return df


if __name__ == "__main__":
    import_all()
