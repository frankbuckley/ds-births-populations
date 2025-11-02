"""Column utilities."""

import pandas as pd
import chance
from fields import Fields

computed_column_types: dict[str, pd.Float64Dtype | pd.CategoricalDtype | pd.CategoricalDtype] = {
    str(Fields.DS): pd.CategoricalDtype(),
    str(Fields.P_DS_LB_NT): pd.Float64Dtype(),
    str(Fields.P_DS_LB_WT): pd.Float64Dtype(),
    str(Fields.CA_DOWN_C): pd.CategoricalDtype(categories=["C", "P", "N", "U"], ordered=False),
    str(Fields.DOWN_IND): pd.CategoricalDtype(),
    str(Fields.DS_C): pd.CategoricalDtype(),
    str(Fields.DS_P): pd.CategoricalDtype(),
    str(Fields.DS_N): pd.CategoricalDtype(),
    str(Fields.DS_U): pd.CategoricalDtype(),
    str(Fields.DS_CORP): pd.CategoricalDtype(),
}

imported_column_types: dict[
    str, pd.Float64Dtype | pd.CategoricalDtype | pd.UInt16Dtype | pd.UInt32Dtype | pd.UInt64Dtype | pd.Int16Dtype | pd.Int32Dtype | pd.Int64Dtype | pd.CategoricalDtype
] = {
    str(Fields.DOB_YY): pd.UInt16Dtype(),
    str(Fields.DOB_MM): pd.CategoricalDtype(),
    str(Fields.BFACIL): pd.CategoricalDtype(),
    str(Fields.F_BFACIL): pd.CategoricalDtype(),
    str(Fields.MAGE_IMPFLG): pd.CategoricalDtype(),
    str(Fields.MAGE_REPFLG): pd.CategoricalDtype(),
    str(Fields.MAGER): pd.CategoricalDtype(),
    str(Fields.DMAGE): pd.CategoricalDtype(),
    str(Fields.MAGER14): pd.CategoricalDtype(),
    str(Fields.MAGER9): pd.CategoricalDtype(),
    str(Fields.MBSTATE_REC): pd.CategoricalDtype(),
    str(Fields.RESTATUS): pd.CategoricalDtype(),
    str(Fields.MRACE31): pd.CategoricalDtype(),
    str(Fields.MRACE6): pd.CategoricalDtype(),
    str(Fields.MRACE15): pd.CategoricalDtype(),
    str(Fields.MRACEIMP): pd.CategoricalDtype(),
    str(Fields.MHISPX): pd.CategoricalDtype(),
    str(Fields.MHISP_R): pd.CategoricalDtype(),
    str(Fields.F_MHISP): pd.CategoricalDtype(),
    str(Fields.MRACEHISP): pd.CategoricalDtype(),
    str(Fields.MAR_P): pd.CategoricalDtype(),
    str(Fields.DMAR): pd.CategoricalDtype(),
    str(Fields.MAR_IMP): pd.CategoricalDtype(),
    str(Fields.F_MAR_P): pd.CategoricalDtype(),
    str(Fields.MEDUC): pd.CategoricalDtype(),
    str(Fields.F_MEDUC): pd.CategoricalDtype(),
    str(Fields.FAGERPT_FLG): pd.CategoricalDtype(),
    str(Fields.FAGECOMB): pd.CategoricalDtype(),
    str(Fields.FAGEREC11): pd.CategoricalDtype(),
    str(Fields.FRACE31): pd.CategoricalDtype(),
    str(Fields.FRACE6): pd.CategoricalDtype(),
    str(Fields.FRACE15): pd.CategoricalDtype(),
    str(Fields.FHISPX): pd.CategoricalDtype(),
    str(Fields.FHISP_R): pd.CategoricalDtype(),
    str(Fields.F_FHISP): pd.CategoricalDtype(),
    str(Fields.FRACEHISP): pd.CategoricalDtype(),
    str(Fields.FEDUC): pd.CategoricalDtype(),
    str(Fields.PRIORLIVE): pd.CategoricalDtype(),
    str(Fields.PRIORDEAD): pd.CategoricalDtype(),
    str(Fields.PRIORTERM): pd.CategoricalDtype(),
    str(Fields.F_MPCB): pd.CategoricalDtype(),
    str(Fields.PRECARE5): pd.CategoricalDtype(),
    str(Fields.PREVIS): pd.CategoricalDtype(),
    str(Fields.PREVIS_REC): pd.CategoricalDtype(),
    str(Fields.F_TPCV): pd.CategoricalDtype(),
    str(Fields.WIC): pd.CategoricalDtype(),
    str(Fields.F_WIC): pd.CategoricalDtype(),
    str(Fields.LBO_REC): pd.CategoricalDtype(),
    str(Fields.TBO_REC): pd.UInt16Dtype(),
    str(Fields.PRECARE): pd.CategoricalDtype(),
    str(Fields.PAY): pd.CategoricalDtype(),
    str(Fields.PAY_REC): pd.CategoricalDtype(),
    str(Fields.F_PAY): pd.CategoricalDtype(),
    str(Fields.F_PAY_REC): pd.CategoricalDtype(),
    str(Fields.SEX): pd.CategoricalDtype(),
    str(Fields.CA_ANEN): pd.CategoricalDtype(),
    str(Fields.CA_MNSB): pd.CategoricalDtype(),
    str(Fields.CA_CCHD): pd.CategoricalDtype(),
    str(Fields.CA_CDH): pd.CategoricalDtype(),
    str(Fields.CA_OMPH): pd.CategoricalDtype(),
    str(Fields.CA_GAST): pd.CategoricalDtype(),
    str(Fields.F_CA_ANEN): pd.CategoricalDtype(),
    str(Fields.F_CA_MENIN): pd.CategoricalDtype(),
    str(Fields.F_CA_HEART): pd.CategoricalDtype(),
    str(Fields.F_CA_HERNIA): pd.CategoricalDtype(),
    str(Fields.F_CA_OMPHA): pd.CategoricalDtype(),
    str(Fields.F_CA_GASTRO): pd.CategoricalDtype(),
    str(Fields.CA_LIMB): pd.CategoricalDtype(),
    str(Fields.CA_CLEFT): pd.CategoricalDtype(),
    str(Fields.CA_CLPAL): pd.CategoricalDtype(),
    str(Fields.DOWNS): pd.CategoricalDtype(),
    str(Fields.UCA_DOWNS): pd.CategoricalDtype(),
    str(Fields.CA_DOWN): pd.CategoricalDtype(categories=["C", "P", "N", "U"], ordered=False),
    str(Fields.CA_DOWNS): pd.CategoricalDtype(categories=["C", "P", "N", "U"], ordered=False),
    str(Fields.CA_DISOR): pd.CategoricalDtype(),
    str(Fields.CA_HYPO): pd.CategoricalDtype(),
    str(Fields.F_CA_LIMB): pd.CategoricalDtype(),
    str(Fields.F_CA_CLEFT): pd.CategoricalDtype(),
    str(Fields.F_CA_CLPAL): pd.CategoricalDtype(),
    str(Fields.F_CA_DOWN): pd.CategoricalDtype(),
    str(Fields.F_CA_DOWNS): pd.CategoricalDtype(),
    str(Fields.F_CA_DISOR): pd.CategoricalDtype(),
    str(Fields.F_CA_HYPO): pd.CategoricalDtype(),
    str(Fields.NO_CONGEN): pd.CategoricalDtype(),
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
            if (dtype == pd.UInt8Dtype()
                    or dtype == pd.UInt16Dtype() or dtype == pd.UInt32Dtype()
                    or dtype == pd.UInt64Dtype() or dtype == pd.Int16Dtype()
                    or dtype == pd.Int32Dtype() or dtype == pd.Int64Dtype()):
                df[col] = pd.to_numeric(df[col], downcast="unsigned").astype(dtype, errors="raise")
            else:
                df[col] = df[col].astype(dtype, errors="raise")
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
    ).astype(pd.CategoricalDtype())

    df[str(Fields.P_DS_LB)] = df[str(Fields.MAGER)].apply(
        lambda x: chance.get_ds_lb_nt_probability(x)
    ).astype(pd.Float64Dtype())

    df[str(Fields.CA_DOWN_C)] = df[str(Fields.CA_DOWN)].fillna(df[str(Fields.CA_DOWNS)])

    df[str(Fields.DS_C)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "C")).astype(pd.CategoricalDtype())
    df[str(Fields.DS_P)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "P")).astype(pd.CategoricalDtype())
    df[str(Fields.DS_N)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "N")).astype(pd.CategoricalDtype())
    df[str(Fields.DS_U)] = df[str(Fields.CA_DOWN_C)].apply(lambda x: is_value(x, "U")).astype(pd.CategoricalDtype())

    df[str(Fields.DS_CORP)] = df[str(Fields.DS_C)].astype(pd.CategoricalDtype()) + df[str(Fields.DS_P)].astype(
        pd.CategoricalDtype())

    df = set_computed_column_types(df)

    return df


def is_confirmed_or_pending(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""
    return 1 if pd.isna(x) else 1 if x in {"P", "C"} else 0


def is_value(x: str, value: str):
    """Check if x is equal to a specific value."""
    return 1 if pd.isna(x) else 1 if x == value else 0
