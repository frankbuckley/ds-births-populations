import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
from variables import Variables as vars


def constrain_pa_series_to_uint8(series: pd.Series, min: int = 0, max: int = 255) -> pd.Series:
    arr = pa.array(series, type=pa.float64())
    arr_i8 = constrain_pa_array_to_uint8(arr, min=min, max=max)
    return pd.Series(arr_i8, dtype="uint8[pyarrow]")


def constrain_pa_series_to_uint16(series: pd.Series, min: int = 0, max: int = 65535) -> pd.Series:
    arr = pa.array(series, type=pa.float64())
    arr_i16 = constrain_pa_array_to_uint16(arr, min=min, max=max)
    return pd.Series(arr_i16, dtype="uint16[pyarrow]")


def constrain_pa_array_to_uint8(arr: pa.Array, min: int = 0, max: int = 255) -> pa.Array:
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


def constrain_pa_array_to_uint16(arr: pa.Array, min: int = 0, max: int = 65535) -> pa.Array:
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

    - if `mrace15` is available, use `mrace6`, 1:1, 2:2, 3:3, 4-14:4, otherwise,
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
