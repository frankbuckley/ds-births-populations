import duckdb
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
from variables import Variables as vars


def load_predictors_data(from_year: int = 1989, to_year: int = 9999) -> pd.DataFrame:
    con = duckdb.connect("./data/us_births.db", read_only=True)

    df = con.execute(
        f"""
        SELECT
            -- (training label) indicated if C or P, not indicated if N, U and missing excluded from training
            CASE
                WHEN COALESCE (ca_down, ca_downs) = 'C' THEN 1::UTINYINT
                WHEN COALESCE (ca_down, ca_downs) = 'P' THEN 1::UTINYINT
                WHEN COALESCE (ca_down, ca_downs) = 'N' THEN 0::UTINYINT
                WHEN uca_downs = 1 THEN 1::UTINYINT
                WHEN uca_downs = 2 THEN 0::UTINYINT
                ELSE NULL
            END AS ca_down_c_p_n,        
            -- ==================== date of birth ====================
            year,
            -- month of birth
            dob_mm,
            -- day of week of birth (1-7)
            dob_wk,
            -- time of birth (0: AM, 1: PM, 2: not stated)
            CASE
                WHEN dob_tt >= 0 AND dob_tt <= 1159 THEN 0::UTINYINT
                WHEN dob_tt >= 1200 AND dob_tt <= 2359 THEN 1::UTINYINT
                WHEN dob_tt = 9999 THEN 2::UTINYINT
                ELSE NULL
            END AS dob_tt_pm,
            -- ==================== birth location ====================
            -- birth place (1: hospital, 2: not hospital, 3: unknown/not stated)
            bfacil3,
            -- ==================== characteristics of baby ====================
            -- sex of baby
            CASE
                WHEN sex = 'M' THEN 1::UTINYINT
                WHEN sex = 'F' THEN 0::UTINYINT
                ELSE NULL
            END AS sex,
            -- birth weight (grams)
            CASE
                WHEN dbwt >= 227 AND dbwt <= 8165 THEN dbwt
                -- we ignore "Not stated" as we treat this variable as numeric rather than categorical
                ELSE NULL
            END AS dbwt,
            -- ==================== characteristics of pregnancy ====================
            -- plurality (1: single... 4 quadpruplet or higher)
            dplural,
            -- month prenatal care began (1 to 10, 0: no prenatal care)
            CASE
                WHEN precare >= 0 AND precare <= 10 THEN precare
                WHEN precare = 99 THEN precare
                ELSE NULL
            END AS precare,
            -- combined gestation estimate
            CASE
                WHEN gestrec10 >= 1 AND gestrec10 <= 10 THEN gestrec10
                WHEN gestrec10 = 99 THEN gestrec10
                ELSE NULL
            END AS gestrec10,
            -- pre-pregnancy weight recode (in pounds)
            CASE
                WHEN pwgt_r >= 75 AND pwgt_r <= 375 THEN pwgt_r
                -- we ignore "Unknown or not stated" as we treat this variable as numeric rather than categorical
                ELSE NULL
            END AS pwgt_r,
            -- weight gain in pounds (98 = 98+)
            CASE
                WHEN wtgain >= 0 AND wtgain <= 98 THEN wtgain
                -- we ignore "Unknown or not stated" as we treat this variable as numeric rather than categorical
                ELSE NULL
            END AS wtgain,
            -- maternal body mass index
            CASE
                WHEN bmi >= 13.0 AND bmi < 69.9 THEN bmi
                -- we ignore "Unknown or not stated" as we treat this variable as numeric rather than categorical
                ELSE NULL
            END
            AS bmi,
            -- ==================== pregnancy risk factors ====================
            -- pre-pregnancy diabetes
            CASE
                WHEN rf_pdiab = 'Y' THEN 1::UTINYINT
                WHEN rf_pdiab = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_pdiab,
            -- gestational diabetes
            CASE
                WHEN rf_gdiab = 'Y' THEN 1::UTINYINT
                WHEN rf_gdiab = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_gdiab,
            -- pre-pregnancy hypertension
            CASE
                WHEN rf_phype = 'Y' THEN 1::UTINYINT
                WHEN rf_phype = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_phype,
            -- gestational hypertension
            CASE
                WHEN rf_ghype = 'Y' THEN 1::UTINYINT
                WHEN rf_ghype = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_ghype,
            -- hypertension eclampsia
            CASE
                WHEN rf_ehype = 'Y' THEN 1::UTINYINT
                WHEN rf_ehype = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_ehype,
            -- previous preterm birth
            CASE
                WHEN rf_ppterm = 'Y' THEN 1::UTINYINT
                WHEN rf_ppterm = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_ppterm,
            -- infertility treatment used
            CASE
                WHEN rf_inftr = 'Y' THEN 1::UTINYINT
                WHEN rf_inftr = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_inftr,
            -- fertility enhancing drugs
            CASE
                WHEN rf_fedrg = 'Y' THEN 1::UTINYINT
                WHEN rf_fedrg = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_fedrg,
            -- asst. reproductive technology
            CASE
                WHEN rf_artec = 'Y' THEN 1::UTINYINT
                WHEN rf_artec = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS rf_artec,
            -- no risk factors reported
            CASE
                WHEN no_risks <= 1 THEN no_risks
                ELSE NULL
            END AS no_risks,
            -- ==================== labor and delivery ====================
            -- induction of labor
            CASE
                WHEN ld_indl = 'Y' THEN 1::UTINYINT
                WHEN ld_indl = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ld_indl,
            -- augmentation of labor
            CASE
                WHEN ld_augm = 'Y' THEN 1::UTINYINT
                WHEN ld_augm = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ld_augm,
            -- fetal presentation at delivery
            CASE
                WHEN me_pres >= 1 AND me_pres <= 3 THEN me_pres
                WHEN me_pres = 9 THEN me_pres
                ELSE NULL
            END AS me_pres,
            -- delivery method recode
            CASE
                WHEN dmeth_rec >= 1 AND dmeth_rec <= 2 THEN dmeth_rec
                WHEN dmeth_rec = 9 THEN dmeth_rec
                ELSE NULL
            END AS dmeth_rec,
            -- ==================== newborn health ====================
            -- five minute apgar score
            CASE
                WHEN apgar5 >= 10 AND apgar5 <= 10 THEN apgar5
                WHEN apgar5 = 99 THEN apgar5
                ELSE NULL
            END AS apgar5,
            -- ten minute apgar score
            CASE
                WHEN apgar10 >= 10 AND apgar10 <= 10 THEN apgar10
                WHEN apgar10 = 99 THEN apgar10
                ELSE NULL
            END AS apgar10,
            -- assisted ventilation (immediately)
            CASE
                WHEN ab_aven1 = 'Y' THEN 1::UTINYINT
                WHEN ab_aven1 = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_aven1,
            -- assisted ventilation > 6 hrs
            CASE
                WHEN ab_aven6 = 'Y' THEN 1::UTINYINT
                WHEN ab_aven6 = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_aven6,
            -- admitted to nicu
            CASE
                WHEN ab_nicu = 'Y' THEN 1::UTINYINT
                WHEN ab_nicu = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_nicu,
            -- surfactant
            CASE
                WHEN ab_surf = 'Y' THEN 1::UTINYINT
                WHEN ab_surf = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_surf,
            -- antibiotics for newborn
            CASE
                WHEN ab_anti = 'Y' THEN 1::UTINYINT
                WHEN ab_anti = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_anti,
            -- seizures
            CASE
                WHEN ab_seiz = 'Y' THEN 1::UTINYINT
                WHEN ab_seiz = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ab_seiz,
            -- no_abnorm
            CASE
                WHEN no_abnorm >= 0 AND no_abnorm <= 1 THEN no_abnorm
                WHEN no_abnorm = 9 THEN no_abnorm
                ELSE NULL
            END AS no_abnorm,
            -- ==================== identified disorders ====================
            -- congenital disorder
            CASE
                WHEN ca_disor = 'C' THEN 1::UTINYINT
                WHEN ca_disor = 'P' THEN 2::UTINYINT
                WHEN ca_disor = 'N' THEN 0::UTINYINT
                ELSE NULL
            END
            AS ca_disor,
            -- anencephaly
            CASE
                WHEN ca_anen = 'Y' THEN 1::UTINYINT
                WHEN ca_anen = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_anen,
            -- meningomyelocele / spina bifida
            CASE
                WHEN ca_mnsb = 'Y' THEN 1::UTINYINT
                WHEN ca_mnsb = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_mnsb,
            -- congenital heart defect
            CASE
                WHEN ca_cchd = 'Y' THEN 1::UTINYINT
                WHEN ca_cchd = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_cchd,
            -- ca_cdh
            CASE
                WHEN ca_cdh = 'Y' THEN 1::UTINYINT
                WHEN ca_cdh = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_cdh,
            -- omphalocele
            CASE
                WHEN ca_omph = 'Y' THEN 1::UTINYINT
                WHEN ca_omph = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_omph,
            -- gastroschisis
            CASE
                WHEN ca_gast = 'Y' THEN 1::UTINYINT
                WHEN ca_gast = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_gast,
            -- limb reduction defect
            CASE
                WHEN ca_limb = 'Y' THEN 1::UTINYINT
                WHEN ca_limb = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_limb,
            -- cleft lip w/ or w/o cleft palate
            CASE
                WHEN ca_cleft = 'Y' THEN 1::UTINYINT
                WHEN ca_cleft = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_cleft,
            -- cleft palate alone
            CASE
                WHEN ca_clpal = 'Y' THEN 1::UTINYINT
                WHEN ca_clpal = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_clpal,
            -- Hypospadias
            CASE
                WHEN ca_hypo = 'Y' THEN 1::UTINYINT
                WHEN ca_hypo = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS ca_hypo,
            -- suspected chromosomal disorder
            CASE
                WHEN ca_disor = 'C' THEN 1::UTINYINT
                WHEN ca_disor = 'P' THEN 2::UTINYINT
                WHEN ca_disor = 'N' THEN 0::UTINYINT
                WHEN ca_disor = 'U' THEN 9::UTINYINT
                ELSE NULL
            END AS ca_disor,
            -- no_congen
            CASE
                WHEN no_congen >= 0 AND no_congen <= 1 THEN no_congen
                WHEN no_congen = 9 THEN no_congen
                ELSE NULL
            END AS no_congen,
            -- ==================== maternal characteristics ====================
            -- maternal age in years
            mage_c,
            -- maternal education
            CASE
                WHEN meduc >= 0 AND meduc < 10 THEN meduc
                ELSE NULL
            END AS meduc,
            -- maternal race
            CASE
                WHEN  mracehisp >= 1 AND mracehisp <= 8 THEN mracehisp
                ELSE NULL
            END AS mracehisp,
            -- ==================== paternal characteristics ====================
            -- father's combined age in years
            CASE
                WHEN fagecomb >= 9 AND fagecomb < 99 THEN fagecomb
                ELSE NULL
            END AS fagecomb,
            -- paternal education
            CASE
                WHEN  feduc < 9 THEN feduc
                ELSE NULL
            END AS feduc,
            -- paternal race
            CASE
                WHEN  fracehisp >= 1 AND fracehisp <= 10 THEN fracehisp
                ELSE NULL
            END AS fracehisp,
            -- ==================== socio-economic indicators ====================
            -- payment source recode
            CASE
                WHEN  pay_rec < 5 THEN pay_rec
                ELSE NULL
            END AS pay_rec,
            -- supplemental nutrition program for women, infants, and children
            CASE
                WHEN wic = 'Y' THEN 1::UTINYINT
                WHEN wic = 'N' THEN 0::UTINYINT
                ELSE NULL
            END AS wic
        FROM
            us_births
        WHERE year >= {from_year} AND year <= {to_year} AND ca_down_c_p_n IS NOT NULL
        ORDER BY
            year, dob_mm, dob_wk
        """
    ).df()

    con.close()

    return df


def constrain_pa_series_to_uint8(
    series: pd.Series, min: int = 0, max: int = 255
) -> pd.Series:
    arr = pa.array(series, type=pa.float64())
    arr_i8 = constrain_pa_array_to_uint8(arr, min=min, max=max)
    return pd.Series(arr_i8, dtype="uint8[pyarrow]")


def constrain_pa_series_to_uint16(
    series: pd.Series, min: int = 0, max: int = 65535
) -> pd.Series:
    arr = pa.array(series, type=pa.float64())
    arr_i16 = constrain_pa_array_to_uint16(arr, min=min, max=max)
    return pd.Series(arr_i16, dtype="uint16[pyarrow]")


def constrain_pa_array_to_uint8(
    arr: pa.Array, min: int = 0, max: int = 255
) -> pa.Array:
    trunc = pc.round(arr, ndigits=0, round_mode="towards_zero")
    is_finite = pc.is_finite(trunc)
    lo = pa.scalar(min, type=pa.float64())
    hi = pa.scalar(max, type=pa.float64())
    ge_lo = pc.greater_equal(trunc, lo)
    le_hi = pc.less_equal(trunc, hi)
    in_range = pc.and_kleene(ge_lo, le_hi)
    keep = pc.and_kleene(is_finite, in_range)
    trunc_masked = pc.if_else(keep, trunc, pa.scalar(None, type=pa.float64()))
    arr_i8 = pc.cast(trunc_masked, pa.uint8(), safe=False)
    return arr_i8


def constrain_pa_array_to_uint16(
    arr: pa.Array, min: int = 0, max: int = 65535
) -> pa.Array:
    trunc = pc.round(arr, ndigits=0, round_mode="towards_zero")
    is_finite = pc.is_finite(trunc)
    lo = pa.scalar(min, type=pa.float64())
    hi = pa.scalar(max, type=pa.float64())
    ge_lo = pc.greater_equal(trunc, lo)
    le_hi = pc.less_equal(trunc, hi)
    in_range = pc.and_kleene(ge_lo, le_hi)
    keep = pc.and_kleene(is_finite, in_range)
    trunc_masked = pc.if_else(keep, trunc, pa.scalar(None, type=pa.float64()))
    arr_i16 = pc.cast(trunc_masked, pa.uint16(), safe=False)
    return arr_i16


def map_mrace(row):
    """

    We set `mrace_c` as follows:

    - if `mrace15` is available, use `mrace15`, 1:1, 2:2, 3:3, 4-14:4, otherwise,
    - if `mracerec` is available, use `mracerec`, 1:1, 2:2, 3:3, 4:4, otherwise,
    - if `mbrace` is available, use `mbrace`, 1:1, 2:2, 3:3, 4:4, otherwise,
    - if `mrace` is available, use `mrace`, 1:1, 2:2, 3:3, 4-78:4, otherwise,
    - missing.

    """
    if not pd.isna(row.get(vars.MRACE15)):
        v = row[vars.MRACE15]
        if v in [1, 2, 3]:
            return v
        elif 4 <= v <= 14:
            return 4
    elif not pd.isna(row.get(vars.MRACEREC)):
        v = row[vars.MRACEREC]
        if v in [1, 2, 3, 4]:
            return v
    elif not pd.isna(row.get(vars.MBRACE)):
        v = row[vars.MBRACE]
        if v in [1, 2, 3, 4]:
            return v
    elif not pd.isna(row.get(vars.MRACE)):
        v = row[vars.MRACE]
        if v in [1, 2, 3]:
            return v
        elif 4 <= v <= 78:
            return 4
    return np.nan


def map_mhisp(row):
    """
    - if `mhispx` is available, then 0:0, 1:1, 2:2, 3:3, 4-6:4, 9:5, otherwise
    - if `mhisp_r` is available, then 0:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
    - if `umhisp` is available, then 0:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
    - if `orracem` is available, then 6-8:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
    - missing
    """
    if not pd.isna(row.get(vars.MHISPX)):
        v = row[vars.MHISPX]
        if v in [0, 1, 2, 3]:
            return v
        elif 4 <= v <= 6:
            return 4
        elif v == 9:
            return 5
    elif not pd.isna(row.get(vars.MHISP_R)):
        v = row[vars.MHISP_R]
        if v in [0, 1, 2, 3]:
            return v
        elif 4 <= v <= 5:
            return 4
        elif v == 9:
            return 5
    elif not pd.isna(row.get(vars.UMHISP)):
        v = row[vars.UMHISP]
        if v in [0, 1, 2, 3]:
            return v
        elif 4 <= v <= 5:
            return 4
        elif v == 9:
            return 5
    elif not pd.isna(row.get(vars.ORRACEM)):
        v = row[vars.ORRACEM]
        if v in [6, 7, 8]:
            return 0
        elif v in [1, 2, 3]:
            return v
        elif 4 <= v <= 5:
            return 4
        elif v == 9:
            return 5
    return np.nan
