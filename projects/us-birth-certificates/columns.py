"""Column utilities."""

import pandas as pd
import chance
from fields import Fields

computed_column_types: dict[
    str, pd.Float64Dtype | pd.UInt8Dtype | pd.CategoricalDtype
] = {
    str(Fields.DS): pd.CategoricalDtype(categories=["Y", "N"], ordered=False),
    str(Fields.DS_LB_CHANCE): pd.Float64Dtype(),
    str(Fields.DS_C): pd.UInt8Dtype(),
}

imported_column_types: dict[
    str, pd.Float64Dtype | pd.UInt8Dtype | pd.UInt16Dtype | pd.CategoricalDtype
] = {
    str(Fields.DOB_YY): pd.UInt16Dtype(),
    str(Fields.DOB_MM): pd.CategoricalDtype(
        categories=[i for i in range(1, 13)], ordered=True
    ),
    str(Fields.BFACIL): pd.CategoricalDtype(
        categories=[i for i in range(1, 10)], ordered=False
    ),
    str(Fields.F_BFACIL): pd.CategoricalDtype(categories=[0, 1], ordered=False),
    str(Fields.MAGE_IMPFLG): pd.CategoricalDtype(),
    str(Fields.MAGE_REPFLG): pd.CategoricalDtype(),
    str(Fields.MAGER): pd.UInt8Dtype(),
    str(Fields.MAGER14): pd.UInt8Dtype(),
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
    str(Fields.LBO_REC): pd.CategoricalDtype(),
    str(Fields.TBO_REC): pd.CategoricalDtype(),
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
    str(Fields.OMPH): pd.CategoricalDtype(),
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
    str(Fields.UCA_DOWNS): pd.CategoricalDtype(
        categories=["Y", "C", "P", "U"], ordered=False
    ),
    str(Fields.CA_DOWN): pd.CategoricalDtype(
        categories=["Y", "C", "P", "U"], ordered=False
    ),
    str(Fields.CA_DISOR): pd.CategoricalDtype(),
    str(Fields.CA_HYPO): pd.CategoricalDtype(),
    str(Fields.F_CA_LIMB): pd.CategoricalDtype(),
    str(Fields.F_CA_CLEFT): pd.CategoricalDtype(),
    str(Fields.F_CA_CLPAL): pd.CategoricalDtype(),
    str(Fields.F_CA_DOWN): pd.CategoricalDtype(),
    str(Fields.F_CA_DISOR): pd.CategoricalDtype(),
    str(Fields.F_CA_HYPO): pd.CategoricalDtype(),
    str(Fields.NO_CONGEN): pd.CategoricalDtype(),
    str(Fields.F_MPCB): pd.CategoricalDtype(),
    str(Fields.PRECARE5): pd.CategoricalDtype(),
    str(Fields.PREVIS): pd.CategoricalDtype(),
    str(Fields.PREVIS_REC): pd.CategoricalDtype(),
    str(Fields.F_TPCV): pd.CategoricalDtype(),
    str(Fields.WIC): pd.CategoricalDtype(),
    str(Fields.F_WIC): pd.CategoricalDtype(),
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


def set_imported_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets imported column types for the dataframe."""

    for col, dtype in imported_column_types.items():
        df[col] = df[col].astype(dtype)
    return df


def set_computed_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets computed column types for the dataframe."""

    for col, dtype in computed_column_types.items():
        df[col] = df[col].astype(dtype)
    return df


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Adds computed columns."""

    df[str(Fields.DS)] = df[str(Fields.CA_DOWN)].apply(lambda x: ds_convert(str(x)))

    df[str(Fields.DS_LB_CHANCE)] = df[str(Fields.MAGER)].apply(
        lambda x: chance.get_ds_lb_chance(x)
    )

    df[str(Fields.DS_C)] = df[str(Fields.CA_DOWN)].apply(lambda x: 1 if x == "C" else 0)

    df[str(Fields.DS_P)] = df[str(Fields.CA_DOWN)].apply(lambda x: 1 if x == "P" else 0)

    df[str(Fields.DS_N)] = df[str(Fields.CA_DOWN)].apply(lambda x: 1 if x == "N" else 0)

    df[str(Fields.DS_U)] = df[str(Fields.CA_DOWN)].apply(lambda x: 1 if x == "U" else 0)

    df[str(Fields.DS_CORP)] = df[str(Fields.DS_C)] + df[str(Fields.DS_P)]

    df = set_computed_column_types(df)

    return df


def ds_convert(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""

    if x in {"P", "C"}:
        return "Y"

    return x
