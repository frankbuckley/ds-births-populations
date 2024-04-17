"""Column utilities."""

import pandas as pd

from .. import calc
from .. import fields

computed_column_types = {
    fields.DS: "category",
    fields.DS_LB_CHANCE: "float64",
}

imported_column_types = {
    fields.DOB_YY: "category",
    fields.DOB_MM: "category",
    fields.BFACIL: "category",
    fields.F_BFACIL: "category",
    fields.MAGE_IMPFLG: "category",
    fields.MAGE_REPFLG: "category",
    fields.MAGER: "category",
    fields.MAGER14: "category",
    fields.MAGER9: "category",
    fields.MBSTATE_REC: "category",
    fields.RESTATUS: "category",
    fields.MRACE31: "category",
    fields.MRACE6: "category",
    fields.MRACE15: "category",
    fields.MRACEIMP: "category",
    fields.MHISPX: "category",
    fields.MHISP_R: "category",
    fields.F_MHISP: "category",
    fields.MRACEHISP: "category",
    fields.MAR_P: "category",
    fields.DMAR: "category",
    fields.MAR_IMP: "category",
    fields.F_MAR_P: "category",
    fields.MEDUC: "category",
    fields.F_MEDUC: "category",
    fields.FAGERPT_FLG: "category",
    fields.FAGECOMB: "category",
    fields.FAGEREC11: "category",
    fields.FRACE31: "category",
    fields.FRACE6: "category",
    fields.FRACE15: "category",
    fields.FHISPX: "category",
    fields.FHISP_R: "category",
    fields.F_FHISP: "category",
    fields.FRACEHISP: "category",
    fields.FEDUC: "category",
    fields.PRIORLIVE: "category",
    fields.PRIORDEAD: "category",
    fields.PRIORTERM: "category",
    fields.LBO_REC: "category",
    fields.TBO_REC: "category",
    fields.PRECARE: "category",
    fields.PAY: "category",
    fields.PAY_REC: "category",
    fields.F_PAY: "category",
    fields.F_PAY_REC: "category",
    fields.SEX: "category",
    fields.IMP_SEX: "category",
    fields.CA_ANEN: "category",
    fields.CA_MNSB: "category",
    fields.CA_CCHD: "category",
    fields.CA_CDH: "category",
    fields.OMPH: "category",
    fields.CA_GAST: "category",
    fields.F_CA_ANEN: "category",
    fields.F_CA_MENIN: "category",
    fields.F_CA_HEART: "category",
    fields.F_CA_HERNIA: "category",
    fields.F_CA_OMPHA: "category",
    fields.F_CA_GASTRO: "category",
    fields.CA_LIMB: "category",
    fields.CA_CLEFT: "category",
    fields.CA_CLPAL: "category",
    fields.CA_DOWN: "category",
    fields.CA_DISOR: "category",
    fields.CA_HYPO: "category",
    fields.F_CA_LIMB: "category",
    fields.F_CA_CLEFT: "category",
    fields.F_CA_CLPAL: "category",
    fields.F_CA_DOWN: "category",
    fields.F_CA_DISOR: "category",
    fields.F_CA_HYPO: "category",
    fields.NO_CONGEN: "category",
    fields.F_MPCB: "category",
    fields.PRECARE5: "category",
    fields.PREVIS: "category",
    fields.PREVIS_REC: "category",
    fields.F_TPCV: "category",
    fields.WIC: "category",
    fields.F_WIC: "category",
}

imported_columns = {
    fields.DOB_YY_INDEX: fields.DOB_YY,
    fields.DOB_MM_INDEX: fields.DOB_MM,
    2: fields.BFACIL,
    3: fields.F_BFACIL,
    4: fields.MAGE_IMPFLG,
    5: fields.MAGE_REPFLG,
    6: fields.MAGER,
    7: fields.MAGER14,
    8: fields.MAGER9,
    9: fields.MBSTATE_REC,
    10: fields.RESTATUS,
    11: fields.MRACE31,
    12: fields.MRACE6,
    13: fields.MRACE15,
    14: fields.MRACEIMP,
    15: fields.MHISPX,
    16: fields.MHISP_R,
    17: fields.F_MHISP,
    18: fields.MRACEHISP,
    19: fields.MAR_P,
    20: fields.DMAR,
    21: fields.MAR_IMP,
    22: fields.F_MAR_P,
    23: fields.MEDUC,
    24: fields.F_MEDUC,
    25: fields.FAGERPT_FLG,
    26: fields.FAGECOMB,
    27: fields.FAGEREC11,
    28: fields.FRACE31,
    29: fields.FRACE6,
    30: fields.FRACE15,
    31: fields.FHISPX,
    32: fields.FHISP_R,
    33: fields.F_FHISP,
    34: fields.FRACEHISP,
    35: fields.FEDUC,
    36: fields.PRIORLIVE,
    37: fields.PRIORDEAD,
    38: fields.PRIORTERM,
    39: fields.LBO_REC,
    40: fields.TBO_REC,
    41: fields.PRECARE,
    42: fields.PAY,
    43: fields.PAY_REC,
    44: fields.F_PAY,
    45: fields.F_PAY_REC,
    46: fields.SEX,
    47: fields.IMP_SEX,
    48: fields.CA_ANEN,
    49: fields.CA_MNSB,
    50: fields.CA_CCHD,
    51: fields.CA_CDH,
    52: fields.OMPH,
    53: fields.CA_GAST,
    54: fields.F_CA_ANEN,
    55: fields.F_CA_MENIN,
    56: fields.F_CA_HEART,
    57: fields.F_CA_HERNIA,
    58: fields.F_CA_OMPHA,
    59: fields.F_CA_GASTRO,
    60: fields.CA_LIMB,
    61: fields.CA_CLEFT,
    62: fields.CA_CLPAL,
    63: fields.CA_DOWN,
    64: fields.CA_DISOR,
    65: fields.CA_HYPO,
    66: fields.F_CA_LIMB,
    67: fields.F_CA_CLEFT,
    68: fields.F_CA_CLPAL,
    69: fields.F_CA_DOWN,
    70: fields.F_CA_DISOR,
    71: fields.F_CA_HYPO,
    72: fields.NO_CONGEN,
    73: fields.F_MPCB,
    74: fields.PRECARE5,
    75: fields.PREVIS,
    76: fields.PREVIS_REC,
    77: fields.F_TPCV,
    78: fields.WIC,
    79: fields.F_WIC,
}


def rename_columns(df: pd.DataFrame, inplace=True) -> pd.DataFrame | None:
    """Renames columns to standard labels."""

    df.rename(columns=imported_columns, inplace=inplace)

    if not inplace:
        return df

    return None


def set_all_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets all (standard + computed) column types for the dataframe."""

    return set_computed_column_types(set_imported_column_types(df))


def set_imported_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets imported column types for the dataframe."""

    return df.astype(imported_column_types)


def set_computed_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets computed column types for the dataframe."""

    return df.astype(computed_column_types)


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Adds computed columns."""

    df[fields.DS] = df[fields.CA_DOWN].apply(lambda x: ds_convert(str(x)))

    df[fields.DS_LB_CHANCE] = df[fields.MAGER].apply(
        lambda x: calc.get_ds_lb_chance(float(x)))

    df = set_computed_column_types(df)

    return df


def ds_convert(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""

    if x in {"P", "C"}:
        return "Y"

    return x
