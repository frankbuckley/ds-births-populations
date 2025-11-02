import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc


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
