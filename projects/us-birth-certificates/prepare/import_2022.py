"""Reads selected columns from 2022 data file and saves to HDF5 file."""

import pandas as pd

import colspecs
import columns


def import_2022():
    "Reads selected columns from 2022 data file and saves to HDF5 file."

    df = pd.read_fwf(
        "data/Nat2022us/Nat2022PublicUS.c20230504.r20230822.txt",
        colspecs=colspecs.colspecs_2022,
        header=None,
        dtype_backend="pyarrow",
    ).convert_dtypes()

    df.attrs["description"] = "Nat2022PublicUS.c20230504.r20230822"

    columns.rename_columns(df)

    df = columns.set_column_types(df)

    df.to_hdf("data/data_2022.h5", key="data_2022", format="table")


if __name__ == "__main__":
    import_2022()
