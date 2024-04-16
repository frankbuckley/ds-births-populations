"""Reads selected columns from all data files and saves to Parquet files."""

import import_2018
import import_2019
import import_2020
import import_2021
import import_2022


def import_all():
    "Reads selected columns from all data files and saves to Parquet files."

    import_2018.import_2018()
    import_2019.import_2019()
    import_2020.import_2020()
    import_2021.import_2021()
    import_2022.import_2022()


if __name__ == "__main__":
    import_all()
