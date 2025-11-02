import chance
import pyarrow as pa
import pandas as pd
from data_utils import constrain_pa_series_to_uint8, constrain_pa_series_to_uint16
from variables import Variables as vars

df = pd.read_parquet("./data/us_births_combined.parquet", dtype_backend="pyarrow")

df[vars.DATAYEAR] = constrain_pa_series_to_uint16(df[vars.DOB_YY], min=1989)
df[vars.DOB_YY] = constrain_pa_series_to_uint16(df[vars.DOB_YY], min=1989)
df[vars.DOB_MM] = constrain_pa_series_to_uint8(df[vars.DOB_MM], min=1, max=12)
df[vars.OSTATE] = df[vars.OSTATE].astype(pd.ArrowDtype(pa.string()))
df[vars.XOSTATE] = df[vars.XOSTATE].astype(pd.ArrowDtype(pa.string()))
df[vars.OCNTYFIPS] = constrain_pa_series_to_uint16(df[vars.OCNTYFIPS])
df[vars.OCNTYPOP] = constrain_pa_series_to_uint8(df[vars.OCNTYPOP])
df[vars.BFACIL] = constrain_pa_series_to_uint8(df[vars.BFACIL], min=1, max=9)
df[vars.F_BFACIL] = constrain_pa_series_to_uint8(df[vars.F_BFACIL], min=0, max=1)
df[vars.UMAGERPT] = constrain_pa_series_to_uint8(df[vars.UMAGERPT])
df[vars.MAGE_IMPFLG] = constrain_pa_series_to_uint8(df[vars.MAGE_IMPFLG], min=0, max=1)
df[vars.MAGE_REPFLG] = constrain_pa_series_to_uint8(pd.to_numeric(df[vars.MAGE_REPFLG], errors="coerce"), min=0, max=1)
df[vars.MAGER] = constrain_pa_series_to_uint8(df[vars.MAGER], min=12, max=50)
df[vars.DMAGE] = constrain_pa_series_to_uint8(df[vars.DMAGE])
df[vars.MAGER41] = constrain_pa_series_to_uint8(df[vars.MAGER41])
df[vars.MAGER14] = constrain_pa_series_to_uint8(df[vars.MAGER14], min=1, max=14)
df[vars.MAGER9] = constrain_pa_series_to_uint8(df[vars.MAGER9], min=1, max=14)
df[vars.UMBSTATE] = df[vars.UMBSTATE].astype(pd.ArrowDtype(pa.string()))
df[vars.MBSTATE_REC] = constrain_pa_series_to_uint8(df[vars.MBSTATE_REC], min=1, max=3)
df[vars.XMRSTATE] = df[vars.XMRSTATE].astype(pd.ArrowDtype(pa.string()))
df[vars.MRSTATE] = df[vars.MRSTATE].astype(pd.ArrowDtype(pa.string()))
df[vars.RCNTY_POP] = df[vars.RCNTY_POP].astype(pd.ArrowDtype(pa.string()))
df[vars.RCITY_POP] = df[vars.RCITY_POP].astype(pd.ArrowDtype(pa.string()))
df[vars.METRORES] = df[vars.METRORES].astype(pd.ArrowDtype(pa.string()))
df[vars.RESTATUS] = constrain_pa_series_to_uint8(df[vars.RESTATUS], min=1, max=2)
df[vars.MBRACE] = df[vars.MBRACE].astype(pd.ArrowDtype(pa.string()))
df[vars.MRACE] = constrain_pa_series_to_uint8(df[vars.MRACE])
df[vars.MRACEREC] = constrain_pa_series_to_uint8(df[vars.MRACEREC])
df[vars.MRACE31] = constrain_pa_series_to_uint8(df[vars.MRACE31], min=1, max=31)
df[vars.MRACE6] = constrain_pa_series_to_uint8(df[vars.MRACE6], min=1, max=6)
df[vars.MRACE15] = constrain_pa_series_to_uint8(df[vars.MRACE15], min=1, max=15)
df[vars.MRACEIMP] = constrain_pa_series_to_uint8(df[vars.MRACEIMP], min=1, max=2)
df[vars.UMHISP] = constrain_pa_series_to_uint8(df[vars.UMHISP])
df[vars.MHISPX] = constrain_pa_series_to_uint8(df[vars.MHISPX], min=0, max=9)
df[vars.MHISP_R] = constrain_pa_series_to_uint8(df[vars.MHISP_R], min=0, max=9)
df[vars.F_MHISP] = constrain_pa_series_to_uint8(df[vars.F_MHISP], min=0, max=1)
df[vars.MRACEHISP] = constrain_pa_series_to_uint8(df[vars.MRACEHISP], min=1, max=8)
df[vars.MAR] = constrain_pa_series_to_uint8(df[vars.MAR])
df[vars.MAR_IMP] = df[vars.MAR_IMP].astype(pd.ArrowDtype(pa.string()))
df[vars.MAR_P] = df[vars.MAR_P].astype(pd.ArrowDtype(pa.string()))
df[vars.DMAR] = df[vars.DMAR].astype(pd.ArrowDtype(pa.string()))
df[vars.F_MAR_P] = constrain_pa_series_to_uint8(df[vars.F_MAR_P], min=0, max=1)
df[vars.MEDUC] = constrain_pa_series_to_uint8(df[vars.MEDUC], min=1, max=9)
df[vars.UMEDUC] = constrain_pa_series_to_uint8(df[vars.UMEDUC])
df[vars.MEDUC_REC] = constrain_pa_series_to_uint8(df[vars.MEDUC_REC])
df[vars.F_MEDUC] = constrain_pa_series_to_uint8(df[vars.F_MEDUC], min=0, max=1)
df[vars.FAGERPT] = constrain_pa_series_to_uint8(df[vars.FAGERPT])
df[vars.UFAGECOMB] = constrain_pa_series_to_uint8(df[vars.UFAGECOMB])
df[vars.FAGERPT_FLG] = df[vars.FAGERPT_FLG].astype(pd.ArrowDtype(pa.string()))
df[vars.FAGECOMB] = constrain_pa_series_to_uint8(df[vars.FAGECOMB], min=0, max=99)
df[vars.FAGEREC11] = constrain_pa_series_to_uint8(df[vars.FAGEREC11], min=0, max=11)
df[vars.FBRACE] = constrain_pa_series_to_uint8(df[vars.FBRACE])
df[vars.FRACEIMP] = constrain_pa_series_to_uint8(df[vars.FRACEIMP])
df[vars.FRACEREC] = constrain_pa_series_to_uint8(df[vars.FRACEREC])
df[vars.UFHISP] = constrain_pa_series_to_uint8(df[vars.UFHISP])
df[vars.FRACEHISP] = constrain_pa_series_to_uint8(df[vars.FRACEHISP], min=1, max=9)
df[vars.FRACE31] = constrain_pa_series_to_uint8(df[vars.FRACE31], min=1, max=99)
df[vars.FRACE6] = constrain_pa_series_to_uint8(df[vars.FRACE6], min=1, max=9)
df[vars.FRACE15] = constrain_pa_series_to_uint8(df[vars.FRACE15], min=1, max=99)
df[vars.FHISPX] = constrain_pa_series_to_uint8(df[vars.FHISPX], min=0, max=9)
df[vars.FHISP_R] = constrain_pa_series_to_uint8(df[vars.FHISP_R], min=0, max=9)
df[vars.F_FHISP] = constrain_pa_series_to_uint8(df[vars.F_FHISP], min=0, max=1)
df[vars.FRACE] = constrain_pa_series_to_uint8(df[vars.FRACE])
df[vars.FEDUC] = constrain_pa_series_to_uint8(df[vars.FEDUC], min=1, max=9)
df[vars.PRIORLIVE] = constrain_pa_series_to_uint8(df[vars.PRIORLIVE], min=0, max=99)
df[vars.PRIORDEAD] = constrain_pa_series_to_uint8(df[vars.PRIORDEAD], min=0, max=99)
df[vars.PRIORTERM] = constrain_pa_series_to_uint8(df[vars.PRIORTERM], min=0, max=99)
df[vars.LBO] = constrain_pa_series_to_uint8(df[vars.LBO])
df[vars.LBO_REC] = constrain_pa_series_to_uint8(df[vars.LBO_REC], min=1, max=9)
df[vars.TBO] = constrain_pa_series_to_uint8(df[vars.TBO])
df[vars.TBO_REC] = constrain_pa_series_to_uint8(df[vars.TBO_REC], min=1, max=9)
df[vars.DLLB_MM] = constrain_pa_series_to_uint8(df[vars.DLLB_MM])
df[vars.DLLB_YY] = constrain_pa_series_to_uint8(df[vars.DLLB_YY])
df[vars.PRECARE] = constrain_pa_series_to_uint8(df[vars.PRECARE], min=1, max=9)
df[vars.PAY] = constrain_pa_series_to_uint8(df[vars.PAY], min=1, max=9)
df[vars.PAY_REC] = constrain_pa_series_to_uint8(df[vars.PAY_REC], min=1, max=9)
df[vars.F_PAY] = constrain_pa_series_to_uint8(df[vars.F_PAY], min=0, max=1)
df[vars.F_PAY_REC] = constrain_pa_series_to_uint8(df[vars.F_PAY_REC], min=0, max=1)
df[vars.SEX] = df[vars.SEX].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_ANEN] = df[vars.CA_ANEN].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_MNSB] = df[vars.CA_MNSB].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_CCHD] = df[vars.CA_CCHD].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_CDH] = df[vars.CA_CDH].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_OMPH] = df[vars.CA_OMPH].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_GAST] = df[vars.CA_GAST].astype(pd.ArrowDtype(pa.string()))
df[vars.F_CA_ANEN] = constrain_pa_series_to_uint8(df[vars.F_CA_ANEN], min=0, max=1)
df[vars.F_CA_MENIN] = constrain_pa_series_to_uint8(df[vars.F_CA_MENIN], min=0, max=1)
df[vars.F_CA_HEART] = constrain_pa_series_to_uint8(df[vars.F_CA_HEART], min=0, max=1)
df[vars.F_CA_HERNIA] = constrain_pa_series_to_uint8(df[vars.F_CA_HERNIA], min=0, max=1)
df[vars.F_CA_OMPHA] = constrain_pa_series_to_uint8(df[vars.F_CA_OMPHA], min=0, max=1)
df[vars.F_CA_GASTRO] = constrain_pa_series_to_uint8(df[vars.F_CA_GASTRO], min=0, max=1)
df[vars.CA_LIMB] = df[vars.CA_LIMB].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_CLEFT] = df[vars.CA_CLEFT].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_CLPAL] = df[vars.CA_CLPAL].astype(pd.ArrowDtype(pa.string()))
df[vars.DOWNS] = constrain_pa_series_to_uint8(df[vars.DOWNS], min=0, max=255)
df[vars.UCA_DOWNS] = constrain_pa_series_to_uint8(df[vars.UCA_DOWNS], min=1, max=9)
df[vars.CA_DOWN] = df[vars.CA_DOWN].astype(pd.ArrowDtype(pa.string()))
df[vars.CA_DOWNS] = df[vars.CA_DOWNS].astype(pd.ArrowDtype(pa.string()))

# combine DATAYEAR and DOB_YY into CA_DOWN_C
df[vars.YEAR] = df[vars.DOB_YY].combine_first(df[vars.DATAYEAR])

# combine CA_DOWN and CA_DOWNS into CA_DOWN_C
df[vars.CA_DOWN_C] = df[vars.CA_DOWN].combine_first(df[vars.CA_DOWNS])

# note: we only have MAGER from 2004. Before then there is DMAGE:
# "This item is: a) computed using dates of birth of mother and of delivery;
# b) reported; or c) imputed. This is the age item used in NCHS publications"
# MAGER41: 01 = <15, 02 = 15, 41 = 54
df[vars.MAGE_C] = df[vars.MAGER].combine_first(df[vars.DMAGE].combine_first(df[vars.MAGER41] + 13))

df[vars.P_DS_LB_NT] = chance.get_ds_lb_nt_probability_array(df[vars.MAGE_C])

prevalence_df = pd.DataFrame({
    vars.DOB_YY: list(range(1989, 2025)),
    vars.P_DS_LB_WT: [
        0.001038,
        0.001055,
        0.001077,
        0.001083,
        0.001093,
        0.001102,
        0.001121,
        0.001099,
        0.001124,
        0.001136,
        0.001153,
        0.001149,
        0.001179,
        0.001216,
        0.001219,
        0.001218,
        0.001236,
        0.001244,
        0.001261,
        0.001257,
        0.001262,
        0.001244,
        0.00127,
        0.001265,
        0.001283,
        0.001302,
        0.001265051,
        0.001295784,
        0.0013375,
        0.001324215,
        0.001324215,
        0.001324215,
        0.001324215,
        0.001324215,
        0.001324215,
        0.001324215,
    ],
})

df = df.merge(prevalence_df, on=vars.DOB_YY, how="left")

df.to_parquet("./data/us_births.parquet")
