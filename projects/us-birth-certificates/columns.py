"""Column utilities."""

import pandas as pd

import chance
import fields


computed_column_types = {
    fields.DS: pd.CategoricalDtype(categories=["Y", "N"], ordered=False),
    fields.DS_LB_CHANCE: pd.Float64Dtype(),
    fields.DS_C: pd.UInt8Dtype(),
}

imported_column_types = {
    fields.DOB_YY: pd.UInt16Dtype(),
    fields.DOB_MM: pd.CategoricalDtype(categories=[i for i in range(1, 13)], ordered=True),
    fields.BFACIL: pd.CategoricalDtype(),
    fields.F_BFACIL: pd.CategoricalDtype(),
    fields.MAGE_IMPFLG: pd.CategoricalDtype(),
    fields.MAGE_REPFLG: pd.CategoricalDtype(),
    fields.MAGER: pd.CategoricalDtype(),
    fields.MAGER14: pd.CategoricalDtype(),
    fields.MAGER9: pd.CategoricalDtype(),
    fields.MBSTATE_REC: pd.CategoricalDtype(),
    fields.RESTATUS: pd.CategoricalDtype(),
    fields.MRACE31: pd.CategoricalDtype(),
    fields.MRACE6: pd.CategoricalDtype(),
    fields.MRACE15: pd.CategoricalDtype(),
    fields.MRACEIMP: pd.CategoricalDtype(),
    fields.MHISPX: pd.CategoricalDtype(),
    fields.MHISP_R: pd.CategoricalDtype(),
    fields.F_MHISP: pd.CategoricalDtype(),
    fields.MRACEHISP: pd.CategoricalDtype(),
    fields.MAR_P: pd.CategoricalDtype(),
    fields.DMAR: pd.CategoricalDtype(),
    fields.MAR_IMP: pd.CategoricalDtype(),
    fields.F_MAR_P: pd.CategoricalDtype(),
    fields.MEDUC: pd.CategoricalDtype(),
    fields.F_MEDUC: pd.CategoricalDtype(),
    fields.FAGERPT_FLG: pd.CategoricalDtype(),
    fields.FAGECOMB: pd.CategoricalDtype(),
    fields.FAGEREC11: pd.CategoricalDtype(),
    fields.FRACE31: pd.CategoricalDtype(),
    fields.FRACE6: pd.CategoricalDtype(),
    fields.FRACE15: pd.CategoricalDtype(),
    fields.FHISPX: pd.CategoricalDtype(),
    fields.FHISP_R: pd.CategoricalDtype(),
    fields.F_FHISP: pd.CategoricalDtype(),
    fields.FRACEHISP: pd.CategoricalDtype(),
    fields.FEDUC: pd.CategoricalDtype(),
    fields.PRIORLIVE: pd.CategoricalDtype(),
    fields.PRIORDEAD: pd.CategoricalDtype(),
    fields.PRIORTERM: pd.CategoricalDtype(),
    fields.LBO_REC: pd.CategoricalDtype(),
    fields.TBO_REC: pd.CategoricalDtype(),
    fields.PRECARE: pd.CategoricalDtype(),
    fields.PAY: pd.CategoricalDtype(),
    fields.PAY_REC: pd.CategoricalDtype(),
    fields.F_PAY: pd.CategoricalDtype(),
    fields.F_PAY_REC: pd.CategoricalDtype(),
    fields.SEX: pd.CategoricalDtype(),
    fields.CA_ANEN: pd.CategoricalDtype(),
    fields.CA_MNSB: pd.CategoricalDtype(),
    fields.CA_CCHD: pd.CategoricalDtype(),
    fields.CA_CDH: pd.CategoricalDtype(),
    fields.OMPH: pd.CategoricalDtype(),
    fields.CA_GAST: pd.CategoricalDtype(),
    fields.F_CA_ANEN: pd.CategoricalDtype(),
    fields.F_CA_MENIN: pd.CategoricalDtype(),
    fields.F_CA_HEART: pd.CategoricalDtype(),
    fields.F_CA_HERNIA: pd.CategoricalDtype(),
    fields.F_CA_OMPHA: pd.CategoricalDtype(),
    fields.F_CA_GASTRO: pd.CategoricalDtype(),
    fields.CA_LIMB: pd.CategoricalDtype(),
    fields.CA_CLEFT: pd.CategoricalDtype(),
    fields.CA_CLPAL: pd.CategoricalDtype(),
    fields.DOWNS: pd.CategoricalDtype(),
    fields.UCA_DOWNS: pd.CategoricalDtype(),
    fields.CA_DOWN: pd.CategoricalDtype(),
    fields.CA_DISOR: pd.CategoricalDtype(),
    fields.CA_HYPO: pd.CategoricalDtype(),
    fields.F_CA_LIMB: pd.CategoricalDtype(),
    fields.F_CA_CLEFT: pd.CategoricalDtype(),
    fields.F_CA_CLPAL: pd.CategoricalDtype(),
    fields.F_CA_DOWN: pd.CategoricalDtype(),
    fields.F_CA_DISOR: pd.CategoricalDtype(),
    fields.F_CA_HYPO: pd.CategoricalDtype(),
    fields.NO_CONGEN: pd.CategoricalDtype(),
    fields.F_MPCB: pd.CategoricalDtype(),
    fields.PRECARE5: pd.CategoricalDtype(),
    fields.PREVIS: pd.CategoricalDtype(),
    fields.PREVIS_REC: pd.CategoricalDtype(),
    fields.F_TPCV: pd.CategoricalDtype(),
    fields.WIC: pd.CategoricalDtype(),
    fields.F_WIC: pd.CategoricalDtype(),
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
