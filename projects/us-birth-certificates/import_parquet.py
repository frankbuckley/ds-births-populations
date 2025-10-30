"""Reads data files and saves to Parquet files."""
import gc
import pathlib
import pandas as pd
import columns


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
        gc.collect()


# TODO: 2018, 2019 import warnings:
#   Python313\Lib\site-packages\pandas\core\dtypes\cast.py:1060: RuntimeWarning: invalid value encountered in cast
#    if (arr.astype(int) == arr).all():


def import_from_sas(source: str, year: int):
    print(f"Importing data for year {year} from {source}...")

    df = pd.read_sas(source, format="sas7bdat", encoding="latin-1").convert_dtypes()

    df = df.reindex(columns=columns.imported_columns)

    columns.ensure_imported_columns(df)
    columns.set_imported_column_types(df)

    # do not compute columns on initial import

    print(f"Saving to data/us_births_{year}.parquet...")

    df.to_parquet(f"data/us_births_{year}.parquet")


if __name__ == "__main__":
    import_all()
