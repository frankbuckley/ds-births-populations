"""Exports data to SPSS format and zips SPSS files."""

from datetime import datetime
import zipfile

import pandas as pd
import pyreadstat as stats


def export_spss():
    "Exports data to SPSS format."

    now = datetime.now().strftime("%Y%m%d_%H%M")

    sources = [
        # "data/us_births_2017.parquet",
        "data/us_births_2018.parquet",
        "data/us_births_2019.parquet",
        "data/us_births_2020.parquet",
        "data/us_births_2021.parquet",
        "data/us_births_2022.parquet"
    ]

    for source in sources:
        dest = source.replace(".parquet", f"_{now}.sav")
        zip_dest = source.replace(".parquet", f"_{now}.zip")

        print(f"Reading {source}...")

        df = pd.read_parquet(source)

        print(f"Exporting to {dest}...")

        stats.write_sav(df, dest)

        print(f"Compressing to {zip_dest}...")

        with zipfile.ZipFile(zip_dest, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as myzip:
            myzip.write(dest)


if __name__ == "__main__":
    export_spss()
