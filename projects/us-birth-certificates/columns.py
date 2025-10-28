"""Column utilities."""

import pandas as pd

import chance
import fields


computed_column_types = {
    fields.DS: "category",
    fields.DS_LB_CHANCE: "float64",
}

imported_column_types = {
    fields.DOB_YY: "int32",
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
    fields.DOWNS: "category",
    fields.UCA_DOWNS: "category",
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

imported_columns = list(imported_column_types.keys())


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
        lambda x: chance.get_ds_lb_chance(x)
    )

    df = set_computed_column_types(df)

    return df


def ds_convert(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""

    if x in {"P", "C"}:
        return "Y"

    return x
