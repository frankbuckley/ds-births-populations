"""Reads selected columns from all data files and saves to Parquet files."""

import pandas as pd

import import_2017
import import_2018
import import_2019
import import_2020
import import_2021
import import_2022


def import_all():
    "Reads selected columns from all data files and saves to Parquet files."

    data_2017 = import_2017.import_2017()
    data_2018 = import_2018.import_2018()
    data_2019 = import_2019.import_2019()
    data_2020 = import_2020.import_2020()
    data_2021 = import_2021.import_2021()
    data_2022 = import_2022.import_2022()

    data_all = pd.concat(
        [data_2017, data_2018, data_2019, data_2020,
            data_2021, data_2022], ignore_index=True
    )

    data_all.to_parquet("data/us_births_all.parquet")


if __name__ == "__main__":
    import_all()
