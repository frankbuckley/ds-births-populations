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
    """Month of birth (01: January... 12: December)"""
    DOB_WK = "dob_wk"
    """Birth day of week (1: Sunday... 7: Saturday)"""
    DOB_TT = "dob_tt"
    """Birth time of day (0000-2359: Time of Birth; 9999: Not Stated)"""
    BFACIL3 = "bfacil3"
    """Birth place recode (1: Hospital, 2: Not in Hospital, 3: Unknown/not stated)"""
    MAGER = "mager"
    """Mother's Single Years of Age"""
    DMAGE = "dmage"
    """Mother's single year of age (pre 2004)"""
    DMAGERPT = "dmagerpt"
    """Reported Age of Mother"""
    MAGER14 = "mager14"
    MAGER9 = "mager9"
    MAGE36 = "mage36"
    MAGER12 = "mager12"
    MAGER8 = "mager8"
    MBSTATE_REC = "mbstate_rec"
    """Mother's Nativity"""
    RESTATUS = "restatus"
    """Mother's Residential Status"""
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
    MRACEHISP = "mracehisp"
    """Mother's Race/Hispanic Origin"""
    MAR = "mar"
    """Mother's Marital Status"""
    MAR_P = "mar_p"
    """Paternity Acknowledged"""
    DMAR = "dmar"
    """Marital Status"""
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
    FEDUC = "feduc"
    PRIORLIVE = "priorlive"
    """Prior Births Now Living"""
    PRIORDEAD = "priordead"
    PRIORTERM = "priorterm"
    LBO_REC = "lbo_rec"
    """Live Birth Order Recode"""
    TBO_REC = "tbo_rec"
    """Total Birth Order Recode"""
    ILLB_R11 = "illb_r11"
    """Interval Since Last Live Birth Recode 11"""
    ILOP_R11 = "ilop_r11"
    """Interval Since Last Other Pregnancy Recode 11"""
    ILP_R11 = "ilp_r11"
    """Interval Since Last Pregnancy Recode 11"""
    PRECARE = "precare"
    """Month Prenatal Care Began"""
    PAY = "pay"
    PAY_REC = "pay_rec"
    APGAR5 = "apgar5"
    """5-Minute Apgar Score"""
    APGAR5R = "apgar5r"
    """5-Minute Apgar Score Recode"""
    APGAR10 = "apgar10"
    """10-Minute Apgar Score"""
    APGAR10R = "apgar10r"
    """10-Minute Apgar Score Recode"""
    DPLURAL = "dplural"
    """Plurality recode"""
    IMP_PLURAL = "imp_plural"
    """Plurality Imputed"""
    SETORDER_R = "setorder_r"
    """Set Order Recode"""
    SEX = "sex"
    """Sex of Infant"""
    GESTREC10 = "gestrec10"
    """Combined Gestation Recode 10"""
    DBWT = "dbwt"
    """Delivery Weight (grams)"""
    DWGT_R = "dwgt_r"
    """Delivery Weight Recode"""
    AB_AVEN1 = "ab_aven1"
    """Assisted Ventilation (immediately)"""
    AB_AVEN6 = "ab_aven6"
    """Assisted Ventilation > 6 hrs"""
    AB_NICU = "ab_nicu"
    """Admitted to NICU"""
    AB_SURF = "ab_surf"
    """Surfactant"""
    AB_ANTI = "ab_anti"
    """Antibiotics for Newborn"""
    AB_SEIZ = "ab_seiz"
    """Seizures"""
    NO_ABNORM = "no_abnorm"
    """No Abnormal Conditions Checked"""
    CA_ANEN = "ca_anen"
    """Anencephaly"""
    CA_MNSB = "ca_mnsb"
    """Meningomyelocele / Spina Bifida"""
    CA_CCHD = "ca_cchd"
    """Cyanotic Congenital Heart Disease"""
    CA_CDH = "ca_cdh"
    """Congenital Diaphragmatic Hernia"""
    CA_OMPH = "ca_omph"
    """Omphalocele"""
    CA_GAST = "ca_gast"
    """Gastroschisis"""
    CA_LIMB = "ca_limb"
    """Limb Reduction Defect"""
    CA_CLEFT = "ca_cleft"
    """Cleft Lip w/ or w/o Cleft Palate"""
    CA_CLPAL = "ca_clpal"
    """Cleft Palate alone"""
    DOWNS = "downs"  # from 1989 to 2002
    UCA_DOWNS = "uca_downs"  # 2003
    CA_DOWN = "ca_down"  # from 2004 onward
    CA_DOWNS = "ca_downs"  # with s 2012 - 2017
    CA_DOWN_C = "ca_down_c"  # combined
    CA_DISOR = "ca_disor"
    CA_HYPO = "ca_hypo"
    NO_CONGEN = "no_congen"
    BFED = "bfed"
    """Breastfed at Discharge"""
    PREVIS = "previs"
    PREVIS_REC = "previs_rec"
    WIC = "wic"
    M_HT_IN = "m_ht_in"
    """Mother's Height in Inches"""
    BMI = "bmi"
    """Body Mass Index"""
    BMI_R = "bmi_r"
    """Body Mass Index Recode"""
    PWGT_R = "pwgt_r"
    """Prepregnancy Weight Recode"""
    WTGAIN = "wtgain"
    """Weight Gain"""
    RF_PDIAB = "rf_pdiab"
    """Prepregnancy Diabetes"""
    RF_GDIAB = "rf_gdiab"
    """Gestational Diabetes"""
    RF_PHYPE = "rf_phype"
    """Prepregnancy Hypertension"""
    RF_GHYPE = "rf_ghype"
    """Gestational Hypertension"""
    RF_EHYPE = "rf_ehype"
    """Hypertension Eclampsia"""
    RF_PPTERM = "rf_ppterm"
    """Previous Preterm Birth"""
    RF_INFTR = "rf_inftr"
    """Infertility Treatment Used"""
    RF_FEDRG = "rf_fedrg"
    """Fertility Drug Use"""
    RF_ARTEC = "rf_artec"
    """Assisted Reproductive Technology"""
    RF_CESAR = "rf_cesar"
    """Previous Cesarean"""
    RF_CESARN = "rf_cesarn"
    """Number of Previous Cesareans"""
    NO_RISKS = "no_risks"
    """No Risk Factors Reported"""
    LD_INDL = "ld_indl"
    """Induction of Labor"""
    LD_AUGM = "ld_augm"
    """Augmentation of Labor"""
    LD_ANES = "ld_anes"
    """Anesthesia"""
    ME_PRES = "me_pres"
    """Fetal Presentation at Delivery"""
    RDMETH_REC = "rdmeth_rec"
    """Delivery Method Recode"""
    DMETH_REC = "dmeth_rec"
    """Delivery Method Recode"""
    ATTEND = "attend"
    """Attendant at Birth"""

    # added/computed columns

    YEAR = "year"

    MAGE_C = "mage_c"

    MRACE_C = "mrace_c"
    MHISP_C = "mhisp_c"
    MRACEHISP_C = "mracehisp_c"

    DOWN_IND = "down_ind"  # DS indicated (DOWNS | UCA_DOWNS | CA_DOWNS | CA_DOWN)

    DS = "ds"  # phase out for DS_CORP

    DS_C = "ds_c"
    DS_P = "ds_p"
    DS_N = "ds_n"
    DS_U = "ds_u"
    DS_CORP = "ds_corp"

    P_DS_LB_WT = "p_ds_lb_wt"
    """
    Probability of Down syndrome live birth with terminations. Estimated from surveillance-based
    prevalence for the given year with no additional adjustments (for maternal age or ethnicity).
    """

    P_DS_LB_NT = "p_ds_lb_nt"
    """
    Probability of Down syndrome live birth absent terminations. Estimated from maternal age
    using Morris formula.
    """

    P_DS_LB_WT_MAGE = "p_ds_lb_wt_mage"
    """
    Probability of Down syndrome live birth with terminations. Estimated from surveillance-based
    prevalence for the given year and maternal age.
    """

    P_DS_LB_NT_MAGE = "p_ds_lb_nt_mage"
    """
    Probability of Down syndrome live birth absent terminations. Estimated from surveillance-based
    prevalence for the given year and maternal age.
    """

    P_DS_LB_WT_ETHN = "p_ds_lb_wt_ethn"
    """
    Probability of Down syndrome live birth with terminations. Estimated from surveillance-based
    prevalence for the given year and ethnicity.
    """

    P_DS_LB_NT_ETHN = "p_ds_lb_nt_ethn"
    """
    Probability of Down syndrome live birth absent terminations. Estimated from surveillance-based
    prevalence for the given year and ethnicity.
    """

    P_DS_LB_WT_MAGE_REDUC = "p_ds_lb_wt_mage_reduc"
    """
    Probability of Down syndrome live birth with terminations. Estimated from surveillance-based
    reduction rate for the given year applied to probability of DS live birth absent terminations,
    estimated from maternal age (P_DS_LB_NT * reduc_rate[year]).
    """


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
    str(Variables.P_DS_LB_WT): pd.Float64Dtype(),
    str(Variables.P_DS_LB_NT): pd.Float64Dtype(),
    str(Variables.P_DS_LB_WT_MAGE): pd.Float64Dtype(),
    str(Variables.P_DS_LB_NT_MAGE): pd.Float64Dtype(),
    str(Variables.P_DS_LB_WT_ETHN): pd.Float64Dtype(),
    str(Variables.P_DS_LB_NT_ETHN): pd.Float64Dtype(),
    str(Variables.P_DS_LB_WT_MAGE_REDUC): pd.Float64Dtype(),
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
    str(Variables.DOB_WK): pd.CategoricalDtype(),
    str(Variables.DOB_TT): pd.CategoricalDtype(),
    str(Variables.BFACIL3): pd.CategoricalDtype(),
    str(Variables.MAGER): pd.CategoricalDtype(),
    str(Variables.DMAGE): pd.CategoricalDtype(),
    str(Variables.DMAGERPT): pd.CategoricalDtype(),
    str(Variables.MAGER14): pd.CategoricalDtype(),
    str(Variables.MAGER9): pd.CategoricalDtype(),
    str(Variables.MAGE36): pd.CategoricalDtype(),
    str(Variables.MAGER12): pd.CategoricalDtype(),
    str(Variables.MBSTATE_REC): pd.CategoricalDtype(),
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
    str(Variables.MRACEHISP): pd.CategoricalDtype(),
    str(Variables.MAR): pd.CategoricalDtype(),
    str(Variables.MAR_P): pd.CategoricalDtype(),
    str(Variables.DMAR): pd.CategoricalDtype(),
    str(Variables.DMEDUC): pd.CategoricalDtype(),
    str(Variables.MEDUC): pd.CategoricalDtype(),
    str(Variables.UMEDUC): pd.CategoricalDtype(),
    str(Variables.MEDUC6): pd.CategoricalDtype(),
    str(Variables.MEDUC_REC): pd.CategoricalDtype(),
    str(Variables.MPLBIR): pd.CategoricalDtype(),
    str(Variables.DFAGE): pd.CategoricalDtype(),
    str(Variables.DFAGERPT): pd.CategoricalDtype(),
    str(Variables.FAGE11): pd.CategoricalDtype(),
    str(Variables.FAGERPT): pd.CategoricalDtype(),
    str(Variables.UFAGECOMB): pd.CategoricalDtype(),
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
    str(Variables.FRACE): pd.CategoricalDtype(),
    str(Variables.FEDUC): pd.CategoricalDtype(),
    str(Variables.PRIORLIVE): pd.CategoricalDtype(),
    str(Variables.PRIORDEAD): pd.CategoricalDtype(),
    str(Variables.PRIORTERM): pd.CategoricalDtype(),
    str(Variables.LBO_REC): pd.CategoricalDtype(),
    str(Variables.TBO_REC): pd.CategoricalDtype(),
    str(Variables.ILLB_R11): pd.CategoricalDtype(),
    str(Variables.ILOP_R11): pd.CategoricalDtype(),
    str(Variables.ILP_R11): pd.CategoricalDtype(),
    str(Variables.PRECARE): pd.CategoricalDtype(),
    str(Variables.PAY): pd.CategoricalDtype(),
    str(Variables.PAY_REC): pd.CategoricalDtype(),
    str(Variables.APGAR5): pd.CategoricalDtype(),
    str(Variables.APGAR5R): pd.CategoricalDtype(),
    str(Variables.APGAR10): pd.CategoricalDtype(),
    str(Variables.APGAR10R): pd.CategoricalDtype(),
    str(Variables.DPLURAL): pd.CategoricalDtype(),
    str(Variables.IMP_PLURAL): pd.CategoricalDtype(),
    str(Variables.SETORDER_R): pd.CategoricalDtype(),
    str(Variables.PREVIS): pd.CategoricalDtype(),
    str(Variables.PREVIS_REC): pd.CategoricalDtype(),
    str(Variables.WIC): pd.CategoricalDtype(),
    str(Variables.SEX): pd.CategoricalDtype(),
    str(Variables.GESTREC10): pd.CategoricalDtype(),
    str(Variables.DBWT): pd.CategoricalDtype(),
    str(Variables.DWGT_R): pd.CategoricalDtype(),
    str(Variables.AB_AVEN1): pd.CategoricalDtype(),
    str(Variables.AB_AVEN6): pd.CategoricalDtype(),
    str(Variables.AB_NICU): pd.CategoricalDtype(),
    str(Variables.AB_SURF): pd.CategoricalDtype(),
    str(Variables.AB_ANTI): pd.CategoricalDtype(),
    str(Variables.AB_SEIZ): pd.CategoricalDtype(),
    str(Variables.NO_ABNORM): pd.CategoricalDtype(),
    str(Variables.CA_ANEN): pd.CategoricalDtype(),
    str(Variables.CA_MNSB): pd.CategoricalDtype(),
    str(Variables.CA_CCHD): pd.CategoricalDtype(),
    str(Variables.CA_CDH): pd.CategoricalDtype(),
    str(Variables.CA_OMPH): pd.CategoricalDtype(),
    str(Variables.CA_GAST): pd.CategoricalDtype(),
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
    str(Variables.NO_CONGEN): pd.CategoricalDtype(),
    str(Variables.BFED): pd.CategoricalDtype(),
    str(Variables.PREVIS): pd.CategoricalDtype(),
    str(Variables.PREVIS_REC): pd.CategoricalDtype(),
    str(Variables.WIC): pd.CategoricalDtype(),
    str(Variables.M_HT_IN): pd.CategoricalDtype(),
    str(Variables.BMI): pd.Float32Dtype(),
    str(Variables.BMI_R): pd.CategoricalDtype(),
    str(Variables.PWGT_R): pd.CategoricalDtype(),
    str(Variables.WTGAIN): pd.CategoricalDtype(),
    str(Variables.RF_PDIAB): pd.CategoricalDtype(),
    str(Variables.RF_GDIAB): pd.CategoricalDtype(),
    str(Variables.RF_PHYPE): pd.CategoricalDtype(),
    str(Variables.RF_GHYPE): pd.CategoricalDtype(),
    str(Variables.RF_EHYPE): pd.CategoricalDtype(),
    str(Variables.RF_PPTERM): pd.CategoricalDtype(),
    str(Variables.RF_INFTR): pd.CategoricalDtype(),
    str(Variables.RF_FEDRG): pd.CategoricalDtype(),
    str(Variables.RF_ARTEC): pd.CategoricalDtype(),
    str(Variables.RF_CESAR): pd.CategoricalDtype(),
    str(Variables.RF_CESARN): pd.CategoricalDtype(),
    str(Variables.NO_RISKS): pd.CategoricalDtype(),
    str(Variables.LD_INDL): pd.CategoricalDtype(),
    str(Variables.LD_AUGM): pd.CategoricalDtype(),
    str(Variables.LD_ANES): pd.CategoricalDtype(),
    str(Variables.ME_PRES): pd.CategoricalDtype(),
    str(Variables.RDMETH_REC): pd.CategoricalDtype(),
    str(Variables.DMETH_REC): pd.CategoricalDtype(),
    str(Variables.ATTEND): pd.CategoricalDtype(),
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
