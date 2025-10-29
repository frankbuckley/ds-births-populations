"""Column utilities."""

import pandas as pd
import chance
from fields import Fields

computed_column_types: dict[str, pd.Float64Dtype | pd.UInt8Dtype | pd.CategoricalDtype] = {
    str(Fields.DS): pd.UInt8Dtype(),
    str(Fields.DS_LB_CHANCE): pd.Float64Dtype(),
    str(Fields.CA_DOWN_C): pd.CategoricalDtype(),
    str(Fields.DS_C): pd.UInt8Dtype(),
    str(Fields.DS_P): pd.UInt8Dtype(),
    str(Fields.DS_N): pd.UInt8Dtype(),
    str(Fields.DS_U): pd.UInt8Dtype(),
    str(Fields.DS_CORP): pd.UInt8Dtype(),
}

imported_column_types: dict[
    str, pd.Float64Dtype | pd.UInt8Dtype | pd.UInt16Dtype | pd.UInt32Dtype | pd.UInt64Dtype | pd.Int16Dtype | pd.Int32Dtype | pd.Int64Dtype | pd.CategoricalDtype
] = {
    str(Fields.DOB_YY): pd.UInt16Dtype(),
    str(Fields.DOB_MM): pd.Int64Dtype(),
    # there some to be data files with floats in this column that convert to greater than
    str(Fields.BFACIL): pd.UInt8Dtype(),
    str(Fields.F_BFACIL): pd.CategoricalDtype(),
    str(Fields.MAGE_IMPFLG): pd.CategoricalDtype(),
    str(Fields.MAGE_REPFLG): pd.CategoricalDtype(),
    str(Fields.MAGER): pd.UInt8Dtype(),
    str(Fields.MAGER14): pd.UInt8Dtype(),
    str(Fields.MAGER9): pd.UInt8Dtype(),
    str(Fields.MBSTATE_REC): pd.UInt8Dtype(),
    str(Fields.RESTATUS): pd.UInt8Dtype(),
    str(Fields.MRACE31): pd.UInt8Dtype(),
    str(Fields.MRACE6): pd.UInt8Dtype(),
    str(Fields.MRACE15): pd.UInt8Dtype(),
    str(Fields.MRACEIMP): pd.UInt8Dtype(),
    str(Fields.MHISPX): pd.UInt8Dtype(),
    str(Fields.MHISP_R): pd.UInt8Dtype(),
    str(Fields.F_MHISP): pd.UInt8Dtype(),
    str(Fields.MRACEHISP): pd.UInt8Dtype(),
    str(Fields.MAR_P): pd.CategoricalDtype(),
    str(Fields.DMAR): pd.CategoricalDtype(),
    str(Fields.MAR_IMP): pd.CategoricalDtype(),
    str(Fields.F_MAR_P): pd.UInt8Dtype(),
    str(Fields.MEDUC): pd.UInt8Dtype(),
    str(Fields.F_MEDUC): pd.UInt8Dtype(),
    str(Fields.FAGERPT_FLG): pd.CategoricalDtype(),
    str(Fields.FAGECOMB): pd.UInt8Dtype(),
    str(Fields.FAGEREC11): pd.UInt8Dtype(),
    str(Fields.FRACE31): pd.UInt8Dtype(),
    str(Fields.FRACE6): pd.UInt8Dtype(),
    str(Fields.FRACE15): pd.UInt8Dtype(),
    str(Fields.FHISPX): pd.UInt8Dtype(),
    str(Fields.FHISP_R): pd.UInt8Dtype(),
    str(Fields.F_FHISP): pd.UInt8Dtype(),
    str(Fields.FRACEHISP): pd.UInt8Dtype(),
    str(Fields.FEDUC): pd.UInt8Dtype(),
    str(Fields.PRIORLIVE): pd.UInt8Dtype(),
    str(Fields.PRIORDEAD): pd.UInt8Dtype(),
    str(Fields.PRIORTERM): pd.UInt8Dtype(),
    str(Fields.F_MPCB): pd.UInt8Dtype(),
    str(Fields.PRECARE5): pd.UInt8Dtype(),
    str(Fields.PREVIS): pd.UInt8Dtype(),
    str(Fields.PREVIS_REC): pd.UInt8Dtype(),
    str(Fields.F_TPCV): pd.UInt8Dtype(),
    str(Fields.WIC): pd.CategoricalDtype(),
    str(Fields.F_WIC): pd.UInt8Dtype(),
    str(Fields.LBO_REC): pd.UInt8Dtype(),
    str(Fields.TBO_REC): pd.UInt16Dtype(),
    str(Fields.PRECARE): pd.UInt8Dtype(),
    str(Fields.PAY): pd.UInt8Dtype(),
    str(Fields.PAY_REC): pd.UInt8Dtype(),
    str(Fields.F_PAY): pd.UInt8Dtype(),
    str(Fields.F_PAY_REC): pd.UInt8Dtype(),
    str(Fields.SEX): pd.CategoricalDtype(),
    str(Fields.CA_ANEN): pd.CategoricalDtype(),
    str(Fields.CA_MNSB): pd.CategoricalDtype(),
    str(Fields.CA_CCHD): pd.CategoricalDtype(),
    str(Fields.CA_CDH): pd.CategoricalDtype(),
    str(Fields.OMPH): pd.CategoricalDtype(),
    str(Fields.CA_GAST): pd.CategoricalDtype(),
    str(Fields.F_CA_ANEN): pd.UInt8Dtype(),
    str(Fields.F_CA_MENIN): pd.UInt8Dtype(),
    str(Fields.F_CA_HEART): pd.UInt8Dtype(),
    str(Fields.F_CA_HERNIA): pd.UInt8Dtype(),
    str(Fields.F_CA_OMPHA): pd.UInt8Dtype(),
    str(Fields.F_CA_GASTRO): pd.UInt8Dtype(),
    str(Fields.CA_LIMB): pd.CategoricalDtype(),
    str(Fields.CA_CLEFT): pd.CategoricalDtype(),
    str(Fields.CA_CLPAL): pd.CategoricalDtype(),
    str(Fields.DOWNS): pd.CategoricalDtype(),
    str(Fields.UCA_DOWNS): pd.CategoricalDtype(),
    str(Fields.CA_DOWN): pd.CategoricalDtype(),
    str(Fields.CA_DOWNS): pd.CategoricalDtype(),
    str(Fields.CA_DISOR): pd.CategoricalDtype(),
    str(Fields.CA_HYPO): pd.CategoricalDtype(),
    str(Fields.F_CA_LIMB): pd.UInt8Dtype(),
    str(Fields.F_CA_CLEFT): pd.UInt8Dtype(),
    str(Fields.F_CA_CLPAL): pd.UInt8Dtype(),
    str(Fields.F_CA_DOWN): pd.UInt8Dtype(),
    str(Fields.F_CA_DOWNS): pd.UInt8Dtype(),
    str(Fields.F_CA_DISOR): pd.UInt8Dtype(),
    str(Fields.F_CA_HYPO): pd.UInt8Dtype(),
    str(Fields.NO_CONGEN): pd.UInt8Dtype(),
}

imported_columns = list(imported_column_types.keys())


def set_all_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets all (standard + computed) column types for the dataframe."""

    return set_computed_column_types(set_imported_column_types(df))


def ensure_imported_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures all imported columns exist in the dataframe."""

    for col in imported_columns:
        if col not in df.columns:
            df[col] = pd.NA

    return df


def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures all imported columns exist in the dataframe."""

    for col in imported_columns:
        if col not in df.columns:
            df[col] = pd.NA

    for col in computed_column_types:
        if col not in df.columns:
            df[col] = pd.NA

    return df


def set_imported_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets imported column types for the dataframe."""

    for col, dtype in imported_column_types.items():
        try:
            # importing 2005: TypeError: Cannot cast array data from dtype('float64') to dtype('uint16')
            if (dtype == pd.UInt16Dtype() or dtype == pd.UInt8Dtype() or dtype == pd.UInt32Dtype()
                    or dtype == pd.UInt64Dtype() or dtype == pd.Int16Dtype() or dtype == pd.Int32Dtype()
                    or dtype == pd.Int64Dtype()):
                df[col] = pd.to_numeric(df[col], downcast="unsigned").astype(dtype)
            else:
                df[col] = df[col].astype(dtype)
        except ValueError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e
        except TypeError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e

    return df


def set_computed_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets computed column types for the dataframe."""

    for col, dtype in computed_column_types.items():
        try:
            df[col] = df[col].astype(dtype)
        except ValueError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e
        except TypeError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e

    return df


def set_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Adds computed columns."""

    df[str(Fields.DS)] = df[str(Fields.CA_DOWN)].apply(
        lambda x: is_confirmed_or_pending(str(x))
    ).astype(pd.UInt8Dtype())

    df[str(Fields.DS_LB_CHANCE)] = df[str(Fields.MAGER)].apply(
        lambda x: chance.get_ds_lb_chance(x)
    ).astype(pd.Float64Dtype())

    df[str(Fields.CA_DOWN_C)] = df[str(Fields.CA_DOWN)].fillna(df[str(Fields.CA_DOWNS)])

    df[str(Fields.DS_C)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "C")).astype(pd.UInt8Dtype())
    df[str(Fields.DS_P)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "P")).astype(pd.UInt8Dtype())
    df[str(Fields.DS_N)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "N")).astype(pd.UInt8Dtype())
    df[str(Fields.DS_U)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "U")).astype(pd.UInt8Dtype())

    df[str(Fields.DS_CORP)] = df[str(Fields.DS_C)].astype(pd.UInt8Dtype()) + df[str(Fields.DS_P)].astype(
        pd.UInt8Dtype())

    df = set_computed_column_types(df)

    return df


def is_confirmed_or_pending(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""
    return 1 if pd.isna(x) else 1 if x in {"P", "C"} else 0


def is_value(x: str, value: str):
    """Check if x is equal to a specific value."""
    return 1 if pd.isna(x) else 1 if x == value else 0
