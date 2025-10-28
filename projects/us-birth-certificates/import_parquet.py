"""Reads data files and saves to Parquet files."""

import pathlib
import pandas as pd
import columns

PARQUET_ENGINE = "fastparquet"


def import_all():
    "Reads data files and saves to Parquet files."

    sources: dict[int, str] = {}

    files = list(pathlib.Path("data").glob("*.sas7bdat"))

    for file in files:
        year_str = "".join(filter(str.isdigit, file.stem))
        if year_str.isdigit():
            if not pathlib.Path(f"data/us_births_{int(year_str)}.parquet").exists():
                year = int(year_str)
                sources[year] = str(file)

    sources = dict(sorted(sources.items(), key=lambda item: item[0], reverse=True))

    for year, source in sources.items():
        import_from_sas(source, year)


def import_from_stata(source: str, year: int):

    print(f"Importing {source}...")

    df = pd.read_stata(
        source,
        preserve_dtypes=False,
        columns=columns.imported_columns,
    ).convert_dtypes()

    print(f"Saving to data/us_births_{year}.parquet...")

    df.to_parquet(f"data/us_births_{year}.parquet", engine=PARQUET_ENGINE)


# TODO: 2018, 2019 import warnings:
#   Python313\Lib\site-packages\pandas\core\dtypes\cast.py:1060: RuntimeWarning: invalid value encountered in cast
#    if (arr.astype(int) == arr).all():


def import_from_sas(source: str, year: int):

    print(f"Importing {source}...")

    df = pd.read_sas(source, format="sas7bdat", encoding="latin-1").convert_dtypes()

    df = df.reindex(columns=columns.imported_columns)

    columns.set_imported_column_types(df)
    columns.add_computed_columns(df)

    print(f"Saving to data/us_births_{year}.parquet...")

    df.to_parquet(f"data/us_births_{year}.parquet", engine=PARQUET_ENGINE)


if __name__ == "__main__":
    import_all()
