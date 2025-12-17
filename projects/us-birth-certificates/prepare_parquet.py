import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.dataset as ds
import pyarrow.parquet as pq

from variables import Variables as vars


def _any_true(mask: pa.Array) -> bool:
    # pc.any can be null if all null; treat as False
    s = pc.any(mask)
    return bool(s.as_py() or False)


_NUMERIC_RE = r"^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$"


def _count_true(mask: pa.Array) -> int:
    # mask is boolean with possible nulls
    s = pc.sum(pc.cast(pc.fill_null(mask, False), pa.int64()))
    return int(s.as_py() or 0)


def constrain_and_cast_uint_robust(
    arr: pa.Array,
    dtype: pa.DataType,
    *,
    min=None,
    max=None,
    non_integer="null",  # "null" or "truncate"
    range_invalid="null",  # "null" or "error"
    stats: dict | None = None,
    stat_key: str | None = None,
) -> pa.Array:
    """
    Robustly cast to an unsigned int dtype.
    - Strings like '1.0' are accepted -> 1
    - Unparseable strings -> null
    - Non-integers (e.g. '1.2') -> null by default
    - Out-of-range -> null by default
    """

    n = len(arr)
    nulls_out = pa.nulls(n, type=dtype)

    # 1) Coerce to float64 in a way that never raises on junk strings
    if pa.types.is_string(arr.type) or pa.types.is_large_string(arr.type):
        s = pc.utf8_trim_whitespace(arr)
        # Treat empty string as null
        s = pc.if_else(pc.equal(s, ""), pa.nulls(n, type=s.type), s)

        numeric_mask = pc.match_substring_regex(s, _NUMERIC_RE)
        s_num = pc.if_else(numeric_mask, s, pa.nulls(n, type=s.type))

        if stats is not None and stat_key is not None:
            stats.setdefault(stat_key, {})
            stats[stat_key]["parse_invalid"] = stats[stat_key].get("parse_invalid", 0) + _count_true(
                pc.invert(pc.fill_null(numeric_mask, False)))

        f = pc.cast(s_num, pa.float64(), safe=False)

    else:
        # Non-string: try cast to float64 (this is safe for ints/floats/bools/nulls)
        f = pc.cast(arr, pa.float64(), safe=False)

    # 2) Handle non-integer values
    if non_integer == "null":
        is_int = pc.equal(f, pc.floor(f))
        if stats is not None and stat_key is not None:
            stats.setdefault(stat_key, {})
            stats[stat_key]["non_integer"] = stats[stat_key].get("non_integer", 0) + _count_true(
                pc.and_(pc.is_valid(f), pc.invert(pc.fill_null(is_int, False))))
        f = pc.if_else(is_int, f, pa.nulls(n, type=pa.float64()))
    elif non_integer == "truncate":
        pass
    else:
        raise ValueError("non_integer must be 'null' or 'truncate'")

    # 3) Cast float -> uint, allowing float->int truncation (safe because we handled non-integers above)
    out = pc.cast(f, dtype, safe=False)

    # 4) Range constraints
    if min is not None:
        bad = pc.less(out, pa.scalar(min, type=dtype))
        if range_invalid == "null":
            if stats is not None and stat_key is not None:
                stats.setdefault(stat_key, {})
                stats[stat_key]["range_invalid"] = stats[stat_key].get("range_invalid", 0) + _count_true(bad)
            out = pc.if_else(bad, nulls_out, out)
        else:
            if _count_true(bad) > 0:
                raise ValueError(f"{stat_key or 'column'}: values below min={min}")

    if max is not None:
        bad = pc.greater(out, pa.scalar(max, type=dtype))
        if range_invalid == "null":
            if stats is not None and stat_key is not None:
                stats.setdefault(stat_key, {})
                stats[stat_key]["range_invalid"] = stats[stat_key].get("range_invalid", 0) + _count_true(bad)
            out = pc.if_else(bad, nulls_out, out)
        else:
            if _count_true(bad) > 0:
                raise ValueError(f"{stat_key or 'column'}: values above max={max}")

    return out


def cast_to(arr: pa.Array, dtype: pa.DataType) -> pa.Array:
    return pc.cast(arr, dtype, safe=False)


INVALID_POLICY = "null"

U8 = pa.uint8()
U16 = pa.uint16()

uint16_specs = {
    vars.DATAYEAR: (1989, None),
    vars.BIRYR: (1989, None),
    vars.DOB_YY: (1989, None),
    vars.DOB_TT: (0, 9999),

    vars.DBWT: (0, 999),
    vars.DWGT_R: (100, 999),
    vars.PWGT_R: (75, 999),
}

uint8_specs = {
    vars.DOB_MM: (1, 12),
    vars.DOB_WK: (1, 7),

    vars.BFACIL3: (1, 3),

    vars.MAGER: (12, 50),
    vars.DMAGE: (None, None),
    vars.DMAGERPT: (None, None),
    vars.MAGER14: (1, 14),
    vars.MAGER9: (1, 14),
    vars.MAGE36: (1, 41),
    vars.MAGER12: (1, 14),
    vars.MAGER8: (1, 9),

    vars.MBSTATE_REC: (1, 3),
    vars.RESTATUS: (1, 4),

    vars.MBRACE: (1, 24),
    vars.MRACE: (None, None),
    vars.MRACEREC: (None, None),
    vars.MRACE31: (1, 31),
    vars.MRACE6: (1, 6),
    vars.MRACE15: (1, 15),
    vars.MRACEIMP: (1, 2),

    vars.ORMOTH: (None, None),
    vars.ORRACEM: (None, None),

    vars.UMHISP: (None, None),
    vars.MHISPX: (0, 9),
    vars.MHISP_R: (0, 9),
    vars.MRACEHISP: (1, 8),

    vars.MAR: (None, None),

    vars.DMEDUC: (None, None),
    vars.MEDUC: (1, 9),
    vars.UMEDUC: (None, None),
    vars.MEDUC6: (None, None),
    vars.MEDUC_REC: (None, None),
    vars.MPLBIR: (None, None),

    vars.DFAGERPT: (None, None),
    vars.FAGE11: (None, None),
    vars.FAGERPT: (None, None),
    vars.UFAGECOMB: (None, None),
    vars.FAGECOMB: (0, 99),
    vars.FAGEREC11: (0, 11),

    vars.ORFATH: (None, None),
    vars.ORRACEF: (None, None),

    vars.FRACE: (None, None),
    vars.FRACEIMP: (None, None),
    vars.FRACEREC: (None, None),

    vars.UFHISP: (None, None),
    vars.FRACEHISP: (1, 9),
    vars.FRACE31: (1, 99),
    vars.FRACE6: (1, 9),
    vars.FRACE15: (1, 99),

    vars.FHISPX: (0, 9),
    vars.FHISP_R: (0, 9),

    vars.FEDUC: (1, 9),

    vars.PRIORLIVE: (0, 99),
    vars.PRIORDEAD: (0, 99),
    vars.PRIORTERM: (0, 99),

    vars.LBO_REC: (1, 9),
    vars.TBO_REC: (1, 9),

    vars.ILLB_R11: (0, 99),
    vars.ILOP_R11: (0, 99),
    vars.ILP_R11: (0, 99),

    vars.PRECARE: (0, 10),

    vars.PAY: (1, 9),
    vars.PAY_REC: (1, 9),

    vars.APGAR5: (0, 99),
    vars.APGAR5R: (1, 5),
    vars.APGAR10: (0, 99),
    vars.APGAR10R: (1, 5),

    vars.DPLURAL: (1, 4),
    vars.IMP_PLURAL: (1, 1),
    vars.SETORDER_R: (1, 9),

    vars.GESTREC10: (1, 99),

    vars.NO_ABNORM: (0, 9),

    vars.DOWNS: (0, 255),
    vars.UCA_DOWNS: (1, 9),
    vars.NO_CONGEN: (0, 1),

    vars.PREVIS: (0, 99),
    vars.PREVIS_REC: (1, 12),

    vars.M_HT_IN: (30, 99),

    vars.BMI_R: (1, 9),
    vars.WTGAIN: (0, 99),

    vars.ME_PRES: (1, 9),
    vars.RDMETH_REC: (1, 9),
    vars.DMETH_REC: (1, 9),
    vars.NO_RISKS: (1, 9),
    vars.ATTEND: (1, 9),
}

string_cols = [
    vars.MAR_P,
    vars.DMAR,
    vars.SEX,
    vars.AB_AVEN1,
    vars.AB_AVEN6,
    vars.AB_NICU,
    vars.AB_SURF,
    vars.AB_ANTI,
    vars.AB_SEIZ,
    vars.CA_ANEN,
    vars.CA_MNSB,
    vars.CA_CCHD,
    vars.CA_CDH,
    vars.CA_OMPH,
    vars.CA_GAST,
    vars.CA_LIMB,
    vars.CA_CLEFT,
    vars.CA_CLPAL,
    vars.CA_DOWN,
    vars.CA_DOWNS,
    vars.CA_DISOR,
    vars.CA_HYPO,
    vars.BFED,
    vars.WIC,
    vars.RF_PDIAB,
    vars.RF_GDIAB,
    vars.RF_PHYPE,
    vars.RF_GHYPE,
    vars.RF_EHYPE,
    vars.RF_PPTERM,
    vars.RF_INFTR,
    vars.RF_FEDRG,
    vars.RF_ARTEC,
    vars.RF_CESAR,
    vars.RF_CESARN,
    vars.LD_INDL,
    vars.LD_AUGM,
    vars.LD_ANES,
]

float16_cols = [
    vars.BMI,
]

stats = {}


def process_batch(batch: pa.RecordBatch) -> pa.RecordBatch:
    arrays = []
    fields = []

    for name, arr in zip(batch.schema.names, batch.columns):
        if name in uint8_specs:
            print(f"Processing uint8 column: {name}")
            mn, mx = uint8_specs[name]
            arr = constrain_and_cast_uint_robust(
                arr,
                U8,
                min=mn,
                max=mx,
                non_integer="null",
                range_invalid="null",
                stats=stats,
                stat_key=name, )
            arrays.append(arr)
            fields.append(pa.field(name, U8))
        elif name in uint16_specs:
            print(f"Processing uint16 column: {name}")
            mn, mx = uint16_specs[name]
            arr = constrain_and_cast_uint_robust(
                arr,
                U16,
                min=mn,
                max=mx,
                non_integer="null",
                range_invalid="null",
                stats=stats,
                stat_key=name, )
            arrays.append(arr)
            fields.append(pa.field(name, U16))
        elif name in string_cols:
            print(f"Processing string column: {name}")
            arr = cast_to(arr, pa.string())
            arrays.append(arr)
            fields.append(pa.field(name, pa.string()))
        elif name in float16_cols:
            print(f"Processing float16 column: {name}")
            arr = cast_to(arr, pa.float16())
            arrays.append(arr)
            fields.append(pa.field(name, pa.float16()))
        else:
            print(f"Warning: Unspecified column '{name}', passing through as-is.")
            arrays.append(arr)
            fields.append(batch.schema.field(name))

    return pa.RecordBatch.from_arrays(arrays, schema=pa.schema(fields))


in_path = "./data/us_births_combined.parquet"
out_path = "./data/us_births.parquet"

dataset = ds.dataset(in_path, format="parquet")

# adjust batch_size as needed based on available memory
scanner = dataset.scanner(batch_size=2_097_152, use_threads=True)

writer = None
try:
    for batch in scanner.to_batches():
        out_batch = process_batch(batch)
        table = pa.Table.from_batches([out_batch])

        if writer is None:
            writer = pq.ParquetWriter(
                out_path,
                table.schema,
                compression="zstd",
                use_dictionary=True,
                write_statistics=True,
            )

        writer.write_table(table, row_group_size=500_000)
finally:
    if writer is not None:
        writer.close()

print("Done.")
