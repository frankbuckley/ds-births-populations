"""Merge annual data files into one."""

import pandas as pd

import columns

PARQUET_ENGINE = "fastparquet"


def merge_years():
    "Merge annual data files into one."

    sources = [
        "data/us_births_2014.parquet",
        "data/us_births_2015.parquet",
        "data/us_births_2016.parquet",
        "data/us_births_2017.parquet",
        "data/us_births_2018.parquet",
        "data/us_births_2019.parquet",
        "data/us_births_2020.parquet",
        "data/us_births_2021.parquet",
        "data/us_births_2022.parquet",
    ]

    dataframes = []

    for source in sources:
        print(f"Reading {source}...")

        df = pd.read_parquet(source)

        df = columns.set_all_column_types(df)

        dataframes.append(df)

    data_all = pd.concat(dataframes)

    data_all.to_parquet("data/us_births_all.parquet", engine=PARQUET_ENGINE)


if __name__ == "__main__":
    merge_years()
