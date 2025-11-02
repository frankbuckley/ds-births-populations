"""Reads data files and saves to Parquet files."""
import gc
import pathlib
import pandas as pd
import variables


def import_all():
    """
    Reads data files and saves to Parquet files.
    """
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


def import_from_sas(source: str, year: int):
    """
    Imports data from a SAS file and saves it as a Parquet file.
    """
    print(f"Importing data for year {year} from {source}...")

    df = pd.read_sas(source, format="sas7bdat", encoding="latin-1")
    df = df.reindex(columns=variables.IMPORTED_VARS)

    print(f"Saving to data/us_births_{year}.parquet...")

    df.to_parquet(f"data/us_births_{year}.parquet")


if __name__ == "__main__":
    import_all()
