"""Column utilities."""

import sys
import pandas as pd

sys.path.append('../us-birth-certificates')

from utils import get_ds_lb_chance

def rename_columns(df: pd.DataFrame, inplace=True) -> pd.DataFrame | None:
    """Renames columns to standard labels."""

    df.rename(
        columns={
            0: "DOB_YY",
            1: "DOB_MM",
            2: "BFACIL",
            3: "F_BFACIL",
            4: "MAGE_IMPFLG",
            5: "MAGE_REPFLG",
            6: "MAGER",
            7: "MAGER14",
            8: "MAGER9",
            9: "MBSTATE_REC",
            10: "RESTATUS",
            11: "MRACE31",
            12: "MRACE6",
            13: "MRACE15",
            14: "MRACEIMP",
            15: "MHISPX",
            16: "MHISP_R",
            17: "F_MHISP",
            18: "MRACEHISP",
            19: "MAR_P",
            20: "DMAR",
            21: "MAR_IMP",
            22: "F_MAR_P",
            23: "MEDUC",
            24: "F_MEDUC",
            25: "FAGERPT_FLG",
            26: "FAGECOMB",
            27: "FAGEREC11",
            28: "FRACE31",
            29: "FRACE6",
            30: "FRACE15",
            31: "FHISPX",
            32: "FHISP_R",
            33: "F_FHISP",
            34: "FRACEHISP",
            35: "FEDUC",
            36: "PRIORLIVE",
            37: "PRIORDEAD",
            38: "PRIORTERM",
            39: "LBO_REC",
            40: "TBO_REC",
            41: "PRECARE",
            42: "PAY",
            43: "PAY_REC",
            44: "F_PAY",
            45: "F_PAY_REC",
            46: "SEX",
            47: "IMP_SEX",
            48: "CA_ANEN",
            49: "CA_MNSB",
            50: "CA_CCHD",
            51: "CA_CDH",
            52: "OMPH",
            53: "CA_GAST",
            54: "F_CA_ANEN",
            55: "F_CA_MENIN",
            56: "F_CA_HEART",
            57: "F_CA_HERNIA",
            58: "F_CA_OMPHA",
            59: "F_CA_GASTRO",
            60: "CA_LIMB",
            61: "CA_CLEFT",
            62: "CA_CLPAL",
            63: "CA_DOWN",
            64: "CA_DISOR",
            65: "CA_HYPO",
            66: "F_CA_LIMB",
            67: "F_CA_CLEFT",
            68: "F_CA_CLPAL",
            69: "F_CA_DOWN",
            70: "F_CA_DISOR",
            71: "F_CA_HYPO",
            72: "NO_CONGEN",
            73: "F_MPCB",
            74: "PRECARE5",
            75: "PREVIS",
            76: "PREVIS_REC",
            77: "F_TPCV",
            78: "WIC",
            79: "F_WIC",
        },
        inplace=inplace,
    )

    if not inplace:
        return df

    return None


def set_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets standard column types for the dataframe."""

    return df.astype({
        "DOB_YY": "int32",
        "DOB_MM": "category",
        "BFACIL": "category",
        "F_BFACIL": "category",
        "MAGE_IMPFLG": "category",
        "MAGE_REPFLG": "category",
        "MAGER": "category",
        "MAGER14": "category",
        "MAGER9": "category",
        "MBSTATE_REC": "category",
        "RESTATUS": "category",
        "MRACE31": "category",
        "MRACE6": "category",
        "MRACE15": "category",
        "MRACEIMP": "category",
        "MHISPX": "category",
        "MHISP_R": "category",
        "F_MHISP": "category",
        "MRACEHISP": "category",
        "MAR_P": "category",
        "DMAR": "category",
        "MAR_IMP": "category",
        "F_MAR_P": "category",
        "MEDUC": "category",
        "F_MEDUC": "category",
        "FAGERPT_FLG": "category",
        "FAGECOMB": "category",
        "FAGEREC11": "category",
        "FRACE31": "category",
        "FRACE6": "category",
        "FRACE15": "category",
        "FHISPX": "category",
        "FHISP_R": "category",
        "F_FHISP": "category",
        "FRACEHISP": "category",
        "FEDUC": "category",
        "PRIORLIVE": "category",
        "PRIORDEAD": "category",
        "PRIORTERM": "category",
        "LBO_REC": "category",
        "TBO_REC": "category",
        "PRECARE": "category",
        "PAY": "category",
        "PAY_REC": "category",
        "F_PAY": "category",
        "F_PAY_REC": "category",
        "SEX": "category",
        "IMP_SEX": "category",
        "CA_ANEN": "category",
        "CA_MNSB": "category",
        "CA_CCHD": "category",
        "CA_CDH": "category",
        "OMPH": "category",
        "CA_GAST": "category",
        "F_CA_ANEN": "category",
        "F_CA_MENIN": "category",
        "F_CA_HEART": "category",
        "F_CA_HERNIA": "category",
        "F_CA_OMPHA": "category",
        "F_CA_GASTRO": "category",
        "CA_LIMB": "category",
        "CA_CLEFT": "category",
        "CA_CLPAL": "category",
        "CA_DOWN": "category",
        "CA_DISOR": "category",
        "CA_HYPO": "category",
        "F_CA_LIMB": "category",
        "F_CA_CLEFT": "category",
        "F_CA_CLPAL": "category",
        "F_CA_DOWN": "category",
        "F_CA_DISOR": "category",
        "F_CA_HYPO": "category",
        "NO_CONGEN": "category",
        "F_MPCB": "category",
        "PRECARE5": "category",
        "PREVIS": "category",
        "PREVIS_REC": "category",
        "F_TPCV": "category",
        "WIC": "category",
        "F_WIC": "category",
    })


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Adds standard computed columns."""

    # DS: combine C (confirmed) and P (pending) from CA_DOWN into Y
    df["DS"] = df["CA_DOWN"].apply(lambda x: ds_convert(str(x)))

    # DS_LB_CHANCE: chance of Down syndrome given mother's age
    # using Moriss et al. (https://doi.org/10.1136/jms.9.1.2)
    df["DS_LB_CHANCE"] = df["MAGER"].apply(
        lambda x: get_ds_lb_chance(float(x)))

    df = df.astype({
        "DS": "category",
        "DS_LB_CHANCE": "float64"
    })

    return df


def ds_convert(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""

    if x in {"P", "C"}:
        return "Y"

    return x
