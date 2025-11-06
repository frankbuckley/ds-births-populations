"""Column utilities."""

import pandas as pd

from enum import StrEnum


class Variables(StrEnum):
    DATAYEAR = "datayear"
    """Data year (older datasets have this)"""
    BIRYR = "biryr"
    """Birth year"""
    DOB_YY = "dob_yy"
    """Year of birth"""
    DOB_MM = "dob_mm"
    """Month of birth"""
    OSTATE = "ostate"
    """Occurrence state"""
    XOSTATE = "xostate"
    """Expanded occurrence state"""
    OCNTYFIPS = "ocntyfips"
    """Occurrence county FIPS code"""
    OCNTYPOP = "ocntypop"
    """Occurrence county population"""
    BFACIL = "bfacil"
    """Birth place"""
    F_BFACIL = "f_bfacil"
    """Reporting flag for birth place"""
    UMAGERPT = "umagerpt"
    """Mother's reported age"""
    MAGE_IMPFLG = "mage_impflg"
    """Mother's Age Imputed: Due to missing data, age imputed"""
    MAGE_REPFLG = "mage_repflg"
    MAGER = "mager"
    """Mother's Single Years of Age"""
    DMAGE = "dmage"
    """Mother's single year of age (pre 2004)"""
    DMAGERPT = "dmagerpt"
    """Reported Age of Mother"""
    MAGER41 = "mager41"
    MAGER14 = "mager14"
    MAGER9 = "mager9"
    MAGE36 = "mage36"
    MAGER12 = "mager12"
    MAGER8 = "mager8"
    UMBSTATE = "umbstate"
    """Mother's Birth State"""
    MBSTATE_REC = "mbstate_rec"
    """Mother's Birth State Recode"""
    XMRSTATE = "xmrstate"
    """Expanded State of Residence of Mother"""
    MRSTATE = "mrstate"
    """Mother's Residence State"""
    RCNTY_POP = "rcnty_pop"
    """Population of Residence County"""
    RCITY_POP = "rcity_pop"
    """Population of Residence City"""
    METRORES = "metrores"
    """Metropolitan Residence County"""
    RESTATUS = "restatus"
    MBRACE = "mbrace"
    """Mother's Bridged Race"""
    MRACE = "mrace"
    """Mother's Race"""
    MRACEREC = "mracerec"
    """Mother's Race Recode"""
    MRACE31 = "mrace31"
    MRACE6 = "mrace6"
    MRACE15 = "mrace15"
    MRACEIMP = "mraceimp"
    """Mother's Race Imputed"""
    ORMOTH = "ormoth"
    """Hispanic Origin of Mother"""
    ORRACEM = "orracem"
    """Hispanic Origin and Race of Mother Recode"""
    UMHISP = "umhisp"
    """Mother's Hispanic Origin"""
    MHISPX = "mhispx"
    MHISP_R = "mhisp_r"
    F_MHISP = "f_mhisp"
    MRACEHISP = "mracehisp"
    """Mother's Race/Hispanic Origin"""
    MAR = "mar"
    """Mother's Marital Status"""
    MAR_IMP = "mar_imp"
    """Mother's Marital Status Imputed"""
    MAR_P = "mar_p"
    DMAR = "dmar"
    F_MAR_P = "f_mar_p"
    DMEDUC = "dmeduc"
    """Education of Mother"""
    MEDUC = "meduc"
    """Mother's Education"""
    UMEDUC = "umeduc"
    """Mother's Education"""
    MEDUC6 = "meduc6"
    """Education of Mother Recode"""
    MEDUC_REC = "meduc_rec"
    """Mother's Education Recode"""
    MPLBIR = "mplbir"
    """Place of Birth of Mother"""
    F_MEDUC = "f_meduc"
    DFAGE = "dfage"
    """Age of Father"""
    DFAGERPT = "dfagerpt"
    """Reported Age of Father"""
    FAGE11 = "fage11"
    """Age of Father Recode"""
    FAGERPT = "fagerpt"
    """Father's Reported Age"""
    UFAGECOMB = "ufagecomb"
    """Father's Combined Age"""
    FAGERPT_FLG = "fagerpt_flg"
    FAGECOMB = "fagecomb"
    FAGEREC11 = "fagerec11"
    """Father's Age Recode 11"""
    FBRACE = "fbrace"
    """Father's Bridged Race"""
    ORFATH = "orfath"
    """Hispanic Origin of Father"""
    ORRACEF = "orracef"
    """Hispanic Origin and Race of Father Recode"""
    FRACE = "frace"
    """Race of Father"""
    FRACEIMP = "fraceimp"
    """Father's Race Imputed"""
    FRACEREC = "fracerec"
    """Father's Race Recode"""
    UFHISP = "ufhisp"
    """Father's Hispanic Origin"""
    FRACEHISP = "fracehisp"
    """Father's Race/Hisp Origin"""
    FRACE31 = "frace31"
    FRACE6 = "frace6"
    FRACE15 = "frace15"
    FHISPX = "fhispx"
    FHISP_R = "fhisp_r"
    F_FHISP = "f_fhisp"
    """Father's Hispanic Origin"""
    FEDUC = "feduc"
    PRIORLIVE = "priorlive"
    """Prior Births Now Living"""
    PRIORDEAD = "priordead"
    PRIORTERM = "priorterm"
    LBO = "lbo"
    LBO_REC = "lbo_rec"
    """Live Birth Order Recode"""
    TBO = "tbo"
    """Total Birth Order"""
    TBO_REC = "tbo_rec"
    DLLB_MM = "dllb_mm"
    """Month of Last Live Birth"""
    DLLB_YY = "dllb_yy"
    """Year of Last Live Birth"""
    PRECARE = "precare"
    """Month Prenatal Care Began"""
    AMNIO = "amnio"
    """Amniocentesis"""
    PAY = "pay"
    PAY_REC = "pay_rec"
    F_PAY = "f_pay"
    F_PAY_REC = "f_pay_rec"
    SEX = "sex"
    CONGENIT = "congenit"
    """Congenital Anomalies"""
    CA_ANEN = "ca_anen"
    CA_MNSB = "ca_mnsb"
    CA_CCHD = "ca_cchd"
    CA_CDH = "ca_cdh"
    CA_OMPH = "ca_omph"
    CA_GAST = "ca_gast"
    F_CA_ANEN = "f_ca_anen"
    F_CA_MENIN = "f_ca_menin"
    F_CA_HEART = "f_ca_heart"
    F_CA_HERNIA = "f_ca_hernia"
    F_CA_OMPHA = "f_ca_ompha"
    F_CA_GASTRO = "f_ca_gastro"
    CA_LIMB = "ca_limb"
    CA_CLEFT = "ca_cleft"
    CA_CLPAL = "ca_clpal"
    DOWNS = "downs"  # from 1989 to 2002
    UCA_DOWNS = "uca_downs"  # 2003
    CA_DOWN = "ca_down"  # from 2004 onward
    CA_DOWNS = "ca_downs"  # with s 2012 - 2017
    CA_DOWN_C = "ca_down_c"  # combined
    CA_DISOR = "ca_disor"
    CA_HYPO = "ca_hypo"
    F_CA_LIMB = "f_ca_limb"
    F_CA_CLEFT = "f_ca_cleftlp"
    F_CA_CLPAL = "f_ca_cleft"
    F_CA_DOWN = "f_ca_down"
    F_CA_DOWNS = "f_ca_downs"
    F_CA_DISOR = "f_ca_chrom"
    F_CA_HYPO = "f_ca_hypos"
    NO_CONGEN = "no_congen"
    F_MPCB = "f_mpcb"
    PRECARE5 = "precare5"
    PREVIS = "previs"
    PREVIS_REC = "previs_rec"
    F_TPCV = "f_tpcv"
    WIC = "wic"
    F_WIC = "f_wic"
    BMI = "bmi"
    """Body Mass Index"""
    BMI_R = "bmi_r"
    """Body Mass Index Recode"""
    PWGT_R = "pwgt_r"
    """Prepregnancy Weight Recode"""
    F_PWGT = "f_pwgt"
    """Reporting Flag for Pre-pregnancy Weight"""
    DWGT_R = "dwgt_r"
    """Delivery Weight Recode"""
    F_DWGT = "f_dwgt"
    """Reporting Flag for Delivery Weight"""

    YEAR = "year"

    MAGE_C = "mage_c"

    MRACE_C = "mrace_c"
    MHISP_C = "mhisp_c"

    DOWN_IND = "down_ind"  # DS indicated (DOWNS | UCA_DOWNS | CA_DOWNS | CA_DOWN)

    DS = "ds"  # phase out for DS_CORP

    DS_C = "ds_c"
    DS_P = "ds_p"
    DS_N = "ds_n"
    DS_U = "ds_u"
    DS_CORP = "ds_corp"

    P_DS_LB_NT = "p_ds_lb_nt"
    """Probability of Down syndrome live birth absent terminations. Estimated from maternal age using Morris formula."""

    P_DS_LB_WT = "p_ds_lb_wt"
    """Probability of Down syndrome live birth with terminations. Estimated from surveillance-based prevalence"""


COMPUTED: dict[
    str, pd.UInt16Dtype | pd.Float64Dtype | pd.CategoricalDtype | pd.CategoricalDtype
] = {
    str(Variables.YEAR): pd.UInt16Dtype(),
    str(Variables.MAGE_C): pd.UInt16Dtype(),
    str(Variables.DS): pd.CategoricalDtype(),
    str(Variables.P_DS_LB_NT): pd.Float64Dtype(),
    str(Variables.P_DS_LB_WT): pd.Float64Dtype(),
    str(Variables.CA_DOWN_C): pd.CategoricalDtype(
        categories=["C", "P", "N", "U"], ordered=False
    ),
    str(Variables.DOWN_IND): pd.CategoricalDtype(),
    str(Variables.DS_C): pd.CategoricalDtype(),
    str(Variables.DS_P): pd.CategoricalDtype(),
    str(Variables.DS_N): pd.CategoricalDtype(),
    str(Variables.DS_U): pd.CategoricalDtype(),
    str(Variables.DS_CORP): pd.CategoricalDtype(),
}

IMPORTED: dict[
    str,
    pd.Float32Dtype
    | pd.Float64Dtype
    | pd.CategoricalDtype
    | pd.UInt16Dtype
    | pd.UInt32Dtype
    | pd.UInt64Dtype
    | pd.Int16Dtype
    | pd.Int32Dtype
    | pd.Int64Dtype
    | pd.CategoricalDtype,
] = {
    str(Variables.DATAYEAR): pd.UInt16Dtype(),
    str(Variables.BIRYR): pd.UInt16Dtype(),
    str(Variables.DOB_YY): pd.UInt16Dtype(),
    str(Variables.DOB_MM): pd.CategoricalDtype(),
    str(Variables.OSTATE): pd.CategoricalDtype(),
    str(Variables.XOSTATE): pd.CategoricalDtype(),
    str(Variables.XOSTATE): pd.CategoricalDtype(),
    str(Variables.OCNTYFIPS): pd.CategoricalDtype(),
    str(Variables.OCNTYPOP): pd.CategoricalDtype(),
    str(Variables.BFACIL): pd.CategoricalDtype(),
    str(Variables.F_BFACIL): pd.CategoricalDtype(),
    str(Variables.UMAGERPT): pd.CategoricalDtype(),
    str(Variables.MAGE_IMPFLG): pd.CategoricalDtype(),
    str(Variables.MAGE_REPFLG): pd.CategoricalDtype(),
    str(Variables.MAGER): pd.CategoricalDtype(),
    str(Variables.DMAGE): pd.CategoricalDtype(),
    str(Variables.DMAGERPT): pd.CategoricalDtype(),
    str(Variables.MAGER41): pd.CategoricalDtype(),
    str(Variables.MAGER14): pd.CategoricalDtype(),
    str(Variables.MAGER9): pd.CategoricalDtype(),
    str(Variables.MAGE36): pd.CategoricalDtype(),
    str(Variables.MAGER12): pd.CategoricalDtype(),
    str(Variables.MAGER8): pd.CategoricalDtype(),
    str(Variables.UMBSTATE): pd.CategoricalDtype(),
    str(Variables.MBSTATE_REC): pd.CategoricalDtype(),
    str(Variables.XMRSTATE): pd.CategoricalDtype(),
    str(Variables.MRSTATE): pd.CategoricalDtype(),
    str(Variables.RCNTY_POP): pd.CategoricalDtype(),
    str(Variables.RCITY_POP): pd.CategoricalDtype(),
    str(Variables.METRORES): pd.CategoricalDtype(),
    str(Variables.RESTATUS): pd.CategoricalDtype(),
    str(Variables.MBRACE): pd.CategoricalDtype(),
    str(Variables.MRACE): pd.CategoricalDtype(),
    str(Variables.MRACEREC): pd.CategoricalDtype(),
    str(Variables.MRACE31): pd.CategoricalDtype(),
    str(Variables.MRACE6): pd.CategoricalDtype(),
    str(Variables.MRACE15): pd.CategoricalDtype(),
    str(Variables.MRACEIMP): pd.CategoricalDtype(),
    str(Variables.ORMOTH): pd.CategoricalDtype(),
    str(Variables.ORRACEM): pd.CategoricalDtype(),
    str(Variables.UMHISP): pd.CategoricalDtype(),
    str(Variables.MHISPX): pd.CategoricalDtype(),
    str(Variables.MHISP_R): pd.CategoricalDtype(),
    str(Variables.F_MHISP): pd.CategoricalDtype(),
    str(Variables.MRACEHISP): pd.CategoricalDtype(),
    str(Variables.MAR): pd.CategoricalDtype(),
    str(Variables.MAR_IMP): pd.CategoricalDtype(),
    str(Variables.MAR_P): pd.CategoricalDtype(),
    str(Variables.DMAR): pd.CategoricalDtype(),
    str(Variables.F_MAR_P): pd.CategoricalDtype(),
    str(Variables.DMEDUC): pd.CategoricalDtype(),
    str(Variables.MEDUC): pd.CategoricalDtype(),
    str(Variables.UMEDUC): pd.CategoricalDtype(),
    str(Variables.MEDUC6): pd.CategoricalDtype(),
    str(Variables.MEDUC_REC): pd.CategoricalDtype(),
    str(Variables.MPLBIR): pd.CategoricalDtype(),
    str(Variables.F_MEDUC): pd.CategoricalDtype(),
    str(Variables.DFAGE): pd.CategoricalDtype(),
    str(Variables.DFAGERPT): pd.CategoricalDtype(),
    str(Variables.FAGE11): pd.CategoricalDtype(),
    str(Variables.FAGERPT): pd.CategoricalDtype(),
    str(Variables.UFAGECOMB): pd.CategoricalDtype(),
    str(Variables.FAGERPT_FLG): pd.CategoricalDtype(),
    str(Variables.FAGECOMB): pd.CategoricalDtype(),
    str(Variables.FAGEREC11): pd.CategoricalDtype(),
    str(Variables.FBRACE): pd.CategoricalDtype(),
    str(Variables.ORFATH): pd.CategoricalDtype(),
    str(Variables.ORRACEF): pd.CategoricalDtype(),
    str(Variables.FRACEIMP): pd.CategoricalDtype(),
    str(Variables.FRACEREC): pd.CategoricalDtype(),
    str(Variables.UFHISP): pd.CategoricalDtype(),
    str(Variables.FRACEHISP): pd.CategoricalDtype(),
    str(Variables.FRACE31): pd.CategoricalDtype(),
    str(Variables.FRACE6): pd.CategoricalDtype(),
    str(Variables.FRACE15): pd.CategoricalDtype(),
    str(Variables.FHISPX): pd.CategoricalDtype(),
    str(Variables.FHISP_R): pd.CategoricalDtype(),
    str(Variables.F_FHISP): pd.CategoricalDtype(),
    str(Variables.FRACE): pd.CategoricalDtype(),
    str(Variables.FEDUC): pd.CategoricalDtype(),
    str(Variables.PRIORLIVE): pd.CategoricalDtype(),
    str(Variables.PRIORDEAD): pd.CategoricalDtype(),
    str(Variables.PRIORTERM): pd.CategoricalDtype(),
    str(Variables.LBO): pd.CategoricalDtype(),
    str(Variables.LBO_REC): pd.CategoricalDtype(),
    str(Variables.TBO): pd.CategoricalDtype(),
    str(Variables.TBO_REC): pd.CategoricalDtype(),
    str(Variables.DLLB_MM): pd.CategoricalDtype(),
    str(Variables.DLLB_YY): pd.CategoricalDtype(),
    str(Variables.PRECARE): pd.CategoricalDtype(),
    str(Variables.AMNIO): pd.CategoricalDtype(),
    str(Variables.PAY): pd.CategoricalDtype(),
    str(Variables.PAY_REC): pd.CategoricalDtype(),
    str(Variables.F_PAY): pd.CategoricalDtype(),
    str(Variables.F_PAY_REC): pd.CategoricalDtype(),
    str(Variables.F_MPCB): pd.CategoricalDtype(),
    str(Variables.PRECARE5): pd.CategoricalDtype(),
    str(Variables.PREVIS): pd.CategoricalDtype(),
    str(Variables.PREVIS_REC): pd.CategoricalDtype(),
    str(Variables.F_TPCV): pd.CategoricalDtype(),
    str(Variables.WIC): pd.CategoricalDtype(),
    str(Variables.F_WIC): pd.CategoricalDtype(),
    str(Variables.SEX): pd.CategoricalDtype(),
    str(Variables.CONGENIT): pd.CategoricalDtype(),
    str(Variables.CA_ANEN): pd.CategoricalDtype(),
    str(Variables.CA_MNSB): pd.CategoricalDtype(),
    str(Variables.CA_CCHD): pd.CategoricalDtype(),
    str(Variables.CA_CDH): pd.CategoricalDtype(),
    str(Variables.CA_OMPH): pd.CategoricalDtype(),
    str(Variables.CA_GAST): pd.CategoricalDtype(),
    str(Variables.F_CA_ANEN): pd.CategoricalDtype(),
    str(Variables.F_CA_MENIN): pd.CategoricalDtype(),
    str(Variables.F_CA_HEART): pd.CategoricalDtype(),
    str(Variables.F_CA_HERNIA): pd.CategoricalDtype(),
    str(Variables.F_CA_OMPHA): pd.CategoricalDtype(),
    str(Variables.F_CA_GASTRO): pd.CategoricalDtype(),
    str(Variables.CA_LIMB): pd.CategoricalDtype(),
    str(Variables.CA_CLEFT): pd.CategoricalDtype(),
    str(Variables.CA_CLPAL): pd.CategoricalDtype(),
    str(Variables.DOWNS): pd.CategoricalDtype(),
    str(Variables.UCA_DOWNS): pd.CategoricalDtype(),
    str(Variables.CA_DOWN): pd.CategoricalDtype(
        categories=["C", "P", "N", "U"], ordered=False
    ),
    str(Variables.CA_DOWNS): pd.CategoricalDtype(
        categories=["C", "P", "N", "U"], ordered=False
    ),
    str(Variables.CA_DISOR): pd.CategoricalDtype(),
    str(Variables.CA_HYPO): pd.CategoricalDtype(),
    str(Variables.F_CA_LIMB): pd.CategoricalDtype(),
    str(Variables.F_CA_CLEFT): pd.CategoricalDtype(),
    str(Variables.F_CA_CLPAL): pd.CategoricalDtype(),
    str(Variables.F_CA_DOWN): pd.CategoricalDtype(),
    str(Variables.F_CA_DOWNS): pd.CategoricalDtype(),
    str(Variables.F_CA_DISOR): pd.CategoricalDtype(),
    str(Variables.F_CA_HYPO): pd.CategoricalDtype(),
    str(Variables.NO_CONGEN): pd.CategoricalDtype(),
    str(Variables.F_MPCB): pd.CategoricalDtype(),
    str(Variables.PRECARE5): pd.CategoricalDtype(),
    str(Variables.PREVIS): pd.CategoricalDtype(),
    str(Variables.PREVIS_REC): pd.CategoricalDtype(),
    str(Variables.F_TPCV): pd.CategoricalDtype(),
    str(Variables.WIC): pd.CategoricalDtype(),
    str(Variables.F_WIC): pd.CategoricalDtype(),
    str(Variables.BMI): pd.Float32Dtype(),
    str(Variables.BMI_R): pd.CategoricalDtype(),
    str(Variables.PWGT_R): pd.CategoricalDtype(),
    str(Variables.F_PWGT): pd.CategoricalDtype(),
    str(Variables.DWGT_R): pd.CategoricalDtype(),
    str(Variables.F_DWGT): pd.CategoricalDtype(),
}

COMPUTED_VARS = list(COMPUTED.keys())
IMPORTED_VARS = list(IMPORTED.keys())


def set_all_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets all (standard + computed) column types for the dataframe."""

    return set_computed_column_types(set_imported_column_types(df))


def ensure_imported_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures all imported columns exist in the dataframe."""

    for col in IMPORTED_VARS:
        if col not in df.columns:
            df[col] = pd.NA

    return df


def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures all imported columns exist in the dataframe."""

    for col in IMPORTED_VARS:
        if col not in df.columns:
            df[col] = pd.NA

    for col in COMPUTED_VARS:
        if col not in df.columns:
            df[col] = pd.NA

    return df


def set_imported_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets imported column types for the dataframe."""

    for col, dtype in IMPORTED.items():
        try:
            # importing 2005: TypeError: Cannot cast array data from dtype('float64') to dtype('uint16')
            if (
                dtype == pd.UInt8Dtype()
                or dtype == pd.UInt16Dtype()
                or dtype == pd.UInt32Dtype()
                or dtype == pd.UInt64Dtype()
                or dtype == pd.Int16Dtype()
                or dtype == pd.Int32Dtype()
                or dtype == pd.Int64Dtype()
            ):
                df[col] = pd.to_numeric(df[col], downcast="unsigned").astype(
                    dtype, errors="raise"
                )
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

    for col, dtype in COMPUTED.items():
        try:
            df[col] = df[col].astype(dtype)
        except ValueError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e
        except TypeError as e:
            print(f"Warning: Could not convert column {col} to type {dtype}.")
            raise e

    return df


def is_confirmed_or_pending(x: str):
    """Combine C (confirmed) and P (pending) into Y value."""
    return 1 if pd.isna(x) else 1 if x in {"P", "C"} else 0


def is_value(x: str, value: str):
    """Check if x is equal to a specific value."""
    return 1 if pd.isna(x) else 1 if x == value else 0
