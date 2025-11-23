import duckdb
import os
import pathlib
import pandas as pd
import shutil
from variables import Variables as vars


def alter_column_type(col: str, new_type: str, con: duckdb.DuckDBPyConnection) -> None:
    print(f"Altering column {col} to {new_type} in us_births...")
    con.execute(
        f"""
        ALTER TABLE us_births
            ALTER {col} TYPE {new_type};
        """
    )


def alter_cast_column_type(
    col: str, new_type: str, con: duckdb.DuckDBPyConnection
) -> None:
    print(f"Altering column {col} to {new_type} with cast in us_births...")
    con.execute(
        f"""
        ALTER TABLE us_births
            ALTER {col} TYPE {new_type} USING CAST({col} AS {new_type});
        """
    )


def alter_try_cast_column_type(
    col: str, new_type: str, con: duckdb.DuckDBPyConnection
) -> None:
    print(f"Altering column {col} to {new_type} with try cast in us_births...")
    con.execute(
        f"""
        ALTER TABLE us_births
            ALTER {col} TYPE {new_type} USING TRY_CAST({col} AS {new_type});
        """
    )


def add_column(col: str, col_type: str, con: duckdb.DuckDBPyConnection) -> None:
    print(f"Adding column {col} to us_births...")
    con.execute(
        f"""
        ALTER TABLE us_births
            ADD COLUMN {col} {col_type};
        """
    )


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_db_temp = src_dir / "us_births_temp.db"
    out_db = src_dir / "us_births.db"

    con = duckdb.connect(out_db_temp.as_posix())

    print("--------------------------------------------------------------")
    print(f"Preparing DuckDB '{out_db_temp}'...")
    print("--------------------------------------------------------------")

    try:
        alter_column_type(vars.DATAYEAR, "USMALLINT", con)
        alter_column_type(vars.BIRYR, "USMALLINT", con)
        alter_column_type(vars.DOB_YY, "USMALLINT", con)
        alter_try_cast_column_type(vars.DOB_MM, "UTINYINT", con)
        alter_try_cast_column_type(vars.DOB_WK, "UTINYINT", con)
        alter_column_type(vars.OSTATE, "VARCHAR", con)
        alter_column_type(vars.XOSTATE, "VARCHAR", con)
        alter_try_cast_column_type(vars.OCNTYFIPS, "USMALLINT", con)
        alter_column_type(vars.OCNTYPOP, "UTINYINT", con)
        alter_column_type(vars.BFACIL, "UTINYINT", con)
        alter_column_type(vars.F_BFACIL, "UTINYINT", con)
        alter_column_type(vars.UMAGERPT, "UTINYINT", con)
        alter_try_cast_column_type(vars.MAGE_IMPFLG, "UTINYINT", con)
        alter_column_type(vars.MAGE_REPFLG, "VARCHAR", con)
        alter_column_type(vars.MAGER, "UTINYINT", con)
        alter_column_type(vars.DMAGE, "UTINYINT", con)
        alter_column_type(vars.DMAGERPT, "UTINYINT", con)
        alter_column_type(vars.MAGER41, "UTINYINT", con)
        alter_try_cast_column_type(vars.MAGER14, "UTINYINT", con)
        alter_column_type(vars.MAGER9, "UTINYINT", con)
        alter_column_type(vars.MAGE36, "UTINYINT", con)
        alter_column_type(vars.MAGER12, "UTINYINT", con)
        alter_column_type(vars.MAGER8, "UTINYINT", con)
        alter_column_type(vars.UMBSTATE, "VARCHAR", con)
        alter_column_type(vars.MBSTATE_REC, "UTINYINT", con)
        alter_column_type(vars.XMRSTATE, "VARCHAR", con)
        alter_column_type(vars.MRSTATE, "VARCHAR", con)
        alter_column_type(vars.RCNTY_POP, "VARCHAR", con)
        alter_column_type(vars.RCITY_POP, "VARCHAR", con)
        alter_column_type(vars.METRORES, "VARCHAR", con)
        alter_column_type(vars.RESTATUS, "UTINYINT", con)
        alter_column_type(vars.MBRACE, "UTINYINT", con)
        alter_column_type(vars.MRACE, "UTINYINT", con)
        alter_column_type(vars.MRACEREC, "UTINYINT", con)
        alter_column_type(vars.MRACE31, "UTINYINT", con)
        alter_column_type(vars.MRACE6, "UTINYINT", con)
        alter_column_type(vars.MRACE15, "UTINYINT", con)
        alter_column_type(vars.MRACEIMP, "UTINYINT", con)
        alter_column_type(vars.ORMOTH, "UTINYINT", con)
        alter_column_type(vars.ORRACEM, "UTINYINT", con)
        alter_column_type(vars.UMHISP, "UTINYINT", con)
        alter_column_type(vars.MHISPX, "UTINYINT", con)
        alter_column_type(vars.MHISP_R, "UTINYINT", con)
        alter_column_type(vars.F_MHISP, "UTINYINT", con)
        alter_try_cast_column_type(vars.MRACEHISP, "UTINYINT", con)
        alter_try_cast_column_type(vars.MAR, "UTINYINT", con)
        alter_column_type(vars.MAR_IMP, "VARCHAR", con)
        alter_column_type(vars.MAR_P, "VARCHAR", con)
        alter_column_type(vars.DMAR, "VARCHAR", con)
        alter_column_type(vars.F_MAR_P, "UTINYINT", con)
        alter_try_cast_column_type(vars.DMEDUC, "UTINYINT", con)
        alter_try_cast_column_type(vars.MEDUC, "UTINYINT", con)
        alter_column_type(vars.UMEDUC, "UTINYINT", con)
        alter_column_type(vars.MEDUC6, "UTINYINT", con)
        alter_try_cast_column_type(vars.MEDUC_REC, "UTINYINT", con)
        alter_column_type(vars.MPLBIR, "UTINYINT", con)
        alter_column_type(vars.F_MEDUC, "UTINYINT", con)
        alter_column_type(vars.DFAGE, "UTINYINT", con)
        alter_column_type(vars.DFAGERPT, "UTINYINT", con)
        alter_column_type(vars.FAGE11, "UTINYINT", con)
        alter_try_cast_column_type(vars.FAGERPT, "UTINYINT", con)
        alter_try_cast_column_type(vars.UFAGECOMB, "UTINYINT", con)
        alter_column_type(vars.FAGERPT_FLG, "VARCHAR", con)
        alter_try_cast_column_type(vars.FAGECOMB, "UTINYINT", con)
        alter_column_type(vars.FAGEREC11, "UTINYINT", con)
        alter_column_type(vars.FBRACE, "UTINYINT", con)
        alter_column_type(vars.ORFATH, "UTINYINT", con)
        alter_column_type(vars.ORRACEF, "UTINYINT", con)
        alter_column_type(vars.FRACE, "UTINYINT", con)
        alter_column_type(vars.FRACEIMP, "UTINYINT", con)
        alter_column_type(vars.FRACEREC, "UTINYINT", con)
        alter_column_type(vars.UFHISP, "UTINYINT", con)
        alter_column_type(vars.FRACEHISP, "UTINYINT", con)
        alter_try_cast_column_type(vars.FRACE31, "UTINYINT", con)
        alter_column_type(vars.FRACE6, "UTINYINT", con)
        alter_column_type(vars.FRACE15, "UTINYINT", con)
        alter_column_type(vars.FHISPX, "UTINYINT", con)
        alter_column_type(vars.FHISP_R, "UTINYINT", con)
        alter_column_type(vars.F_FHISP, "UTINYINT", con)
        alter_column_type(vars.FEDUC, "UTINYINT", con)
        alter_column_type(vars.PRIORLIVE, "UTINYINT", con)
        alter_column_type(vars.PRIORDEAD, "UTINYINT", con)
        alter_column_type(vars.PRIORTERM, "UTINYINT", con)
        alter_column_type(vars.LBO, "UTINYINT", con)
        alter_column_type(vars.LBO_REC, "UTINYINT", con)
        alter_try_cast_column_type(vars.TBO, "UTINYINT", con)
        alter_try_cast_column_type(vars.TBO_REC, "UTINYINT", con)
        alter_try_cast_column_type(vars.ILLB_R, "UTINYINT", con)
        alter_try_cast_column_type(vars.ILLB_R11, "UTINYINT", con)
        alter_column_type(vars.ILLB_R, "UTINYINT", con)
        alter_try_cast_column_type(vars.DLLB_MM, "UTINYINT", con)
        alter_try_cast_column_type(vars.DLLB_YY, "USMALLINT", con)
        alter_column_type(vars.PRECARE, "UTINYINT", con)
        alter_column_type(vars.AMNIO, "UTINYINT", con)
        alter_column_type(vars.PAY, "UTINYINT", con)
        alter_column_type(vars.PAY_REC, "UTINYINT", con)
        alter_column_type(vars.F_PAY, "UTINYINT", con)
        alter_column_type(vars.F_PAY_REC, "UTINYINT", con)
        alter_column_type(vars.APGAR5, "UTINYINT", con)
        alter_try_cast_column_type(vars.APGAR5R, "UTINYINT", con)
        alter_column_type(vars.F_APGAR5, "UTINYINT", con)
        alter_column_type(vars.APGAR10, "UTINYINT", con)
        alter_try_cast_column_type(vars.DPLURAL, "UTINYINT", con)
        alter_column_type(vars.IMP_PLURAL, "UTINYINT", con)
        alter_try_cast_column_type(vars.SETORDER_R, "UTINYINT", con)
        alter_column_type(vars.SEX, "VARCHAR", con)
        alter_column_type(vars.COMBGEST, "UTINYINT", con)
        alter_try_cast_column_type(vars.GESTREC10, "UTINYINT", con)
        alter_try_cast_column_type(vars.LMPUSED, "UTINYINT", con)
        alter_column_type(vars.OEGEST_COMB, "UTINYINT", con)
        alter_column_type(vars.OEGEST_R10, "UTINYINT", con)
        alter_try_cast_column_type(vars.OEGEST_R3, "UTINYINT", con)
        alter_try_cast_column_type(vars.DBWT, "USMALLINT", con)
        alter_column_type(vars.BWTR12, "UTINYINT", con)
        alter_column_type(vars.BWTR4, "UTINYINT", con)
        alter_try_cast_column_type(vars.DWGT_R, "USMALLINT", con)
        alter_column_type(vars.F_DWGT, "UTINYINT", con)
        alter_column_type(vars.AB_AVEN1, "VARCHAR", con)
        alter_column_type(vars.AB_AVEN6, "VARCHAR", con)
        alter_column_type(vars.AB_NICU, "VARCHAR", con)
        alter_column_type(vars.AB_SURF, "VARCHAR", con)
        alter_column_type(vars.AB_ANTI, "VARCHAR", con)
        alter_column_type(vars.AB_SEIZ, "VARCHAR", con)
        alter_column_type(vars.NO_ABNORM, "UTINYINT", con)
        alter_column_type(vars.CONGENIT, "VARCHAR", con)
        alter_column_type(vars.CA_ANEN, "VARCHAR", con)
        alter_column_type(vars.CA_MNSB, "VARCHAR", con)
        alter_column_type(vars.CA_CCHD, "VARCHAR", con)
        alter_column_type(vars.CA_ANEN, "VARCHAR", con)
        alter_column_type(vars.CA_MNSB, "VARCHAR", con)
        alter_column_type(vars.CA_CCHD, "VARCHAR", con)
        alter_column_type(vars.CA_CDH, "VARCHAR", con)
        alter_column_type(vars.CA_OMPH, "VARCHAR", con)
        alter_column_type(vars.CA_GAST, "VARCHAR", con)
        alter_column_type(vars.F_CA_ANEN, "UTINYINT", con)
        alter_column_type(vars.F_CA_MENIN, "UTINYINT", con)
        alter_column_type(vars.F_CA_HEART, "UTINYINT", con)
        alter_column_type(vars.F_CA_HERNIA, "UTINYINT", con)
        alter_column_type(vars.F_CA_OMPHA, "UTINYINT", con)
        alter_column_type(vars.F_CA_GASTRO, "UTINYINT", con)
        alter_column_type(vars.CA_LIMB, "VARCHAR", con)
        alter_column_type(vars.CA_CLEFT, "VARCHAR", con)
        alter_column_type(vars.CA_CLPAL, "VARCHAR", con)
        alter_column_type(vars.DOWNS, "UTINYINT", con)
        alter_column_type(vars.CA_DOWN, "VARCHAR", con)
        alter_column_type(vars.CA_DOWNS, "VARCHAR", con)
        alter_column_type(vars.CA_DISOR, "VARCHAR", con)
        alter_column_type(vars.CA_HYPO, "VARCHAR", con)
        alter_column_type(vars.F_CA_LIMB, "UTINYINT", con)
        alter_column_type(vars.F_CA_CLEFT, "UTINYINT", con)
        alter_column_type(vars.F_CA_CLPAL, "UTINYINT", con)
        alter_column_type(vars.F_CA_DOWN, "UTINYINT", con)
        alter_column_type(vars.F_CA_DISOR, "UTINYINT", con)
        alter_column_type(vars.F_CA_HYPO, "UTINYINT", con)
        alter_try_cast_column_type(vars.NO_CONGEN, "UTINYINT", con)
        alter_column_type(vars.BFED, "VARCHAR", con)
        alter_try_cast_column_type(vars.F_MPCB, "UTINYINT", con)
        alter_column_type(vars.PRECARE5, "UTINYINT", con)
        alter_column_type(vars.PREVIS, "UTINYINT", con)
        alter_try_cast_column_type(vars.PREVIS_REC, "UTINYINT", con)
        alter_try_cast_column_type(vars.F_TPCV, "UTINYINT", con)
        alter_column_type(vars.WIC, "VARCHAR", con)
        alter_try_cast_column_type(vars.F_WIC, "UTINYINT", con)
        alter_column_type(vars.M_HT_IN, "UTINYINT", con)
        alter_column_type(vars.BMI, "FLOAT", con)
        alter_column_type(vars.BMI_R, "USMALLINT", con)
        alter_column_type(vars.PWGT_R, "USMALLINT", con)
        alter_column_type(vars.F_PWGT, "USMALLINT", con)
        alter_column_type(vars.WTGAIN, "UTINYINT", con)
        alter_try_cast_column_type(vars.WTGAIN_REC, "UTINYINT", con)
        alter_column_type(vars.RF_PPTERM, "VARCHAR", con)
        alter_column_type(vars.RF_INFTRM, "VARCHAR", con)
        alter_column_type(vars.RF_FEDRG, "VARCHAR", con)
        alter_column_type(vars.RF_ARTEC, "VARCHAR", con)
        alter_column_type(vars.RF_CESARE, "VARCHAR", con)
        alter_column_type(vars.NO_RISKS, "UTINYINT", con)
        alter_column_type(vars.LD_INDL, "VARCHAR", con)
        alter_column_type(vars.LD_AUGM, "VARCHAR", con)
        alter_column_type(vars.ME_PRES, "VARCHAR", con)
        alter_column_type(vars.ME_ROUTE, "VARCHAR", con)
        alter_column_type(vars.ME_TRIAL, "VARCHAR", con)
        alter_column_type(vars.RDMETH_REC, "UTINYINT", con)
        alter_column_type(vars.DMETH_REC, "UTINYINT", con)
        alter_column_type(vars.ATTEND, "UTINYINT", con)

        add_column(vars.YEAR, "USMALLINT", con)
        add_column(vars.MAGE_C, "UTINYINT", con)
        add_column(vars.MRACE_C, "UTINYINT", con)
        add_column(vars.MHISP_C, "UTINYINT", con)
        add_column(vars.MRACEHISP_C, "UTINYINT", con)
        add_column(vars.DOWN_IND, "UTINYINT", con)
        add_column(vars.CA_DOWN_C, "VARCHAR", con)
        add_column(vars.P_DS_LB_WT, "DOUBLE", con)
        add_column(vars.P_DS_LB_NT, "DOUBLE", con)
        add_column(vars.P_DS_LB_WT_MAGE, "DOUBLE", con)
        add_column(vars.P_DS_LB_NT_MAGE, "DOUBLE", con)
        add_column(vars.P_DS_LB_WT_ETHN, "DOUBLE", con)
        add_column(vars.P_DS_LB_NT_ETHN, "DOUBLE", con)
        add_column(vars.P_DS_LB_WT_MAGE_REDUC, "DOUBLE", con)

        print("Setting mrace_c...")

        con.execute(
            f"""
            UPDATE us_births
            SET {vars.MRACE_C} = CASE
                WHEN {vars.MRACE15} IS NOT NULL AND (year < 2014 OR year > 2019) THEN
                    CASE
                        WHEN {vars.MRACE15} IN(1, 2, 3) THEN {vars.MRACE15}
                        WHEN {vars.MRACE15} BETWEEN 4 AND 14 THEN 4
                    END
                WHEN {vars.MRACEREC} IS NOT NULL AND (year < 2014 OR year > 2019) THEN
                    CASE
                        WHEN {vars.MRACEREC} IN(1, 2, 3, 4) THEN {vars.MRACEREC}
                    END
                WHEN {vars.MBRACE} IS NOT NULL THEN
                    CASE
                        WHEN {vars.MBRACE} IN(1, 2, 3, 4) THEN {vars.MBRACE}
                    END
                WHEN {vars.MRACE} IS NOT NULL THEN
                    CASE
                        WHEN {vars.MRACE} IN(1, 2, 3) THEN {vars.MRACE}
                        WHEN {vars.MRACE} BETWEEN 4 AND 78 THEN 4
                    END
                ELSE NULL
            END
            """
        )

        print("Setting mhisp_c...")

        con.execute(
            f"""
            UPDATE us_births
            SET {vars.MHISP_C} = CASE
                WHEN {vars.MHISP_R} IS NOT NULL THEN
                    CASE
                        WHEN {vars.MHISP_R} IN (0, 1, 2, 3) THEN {vars.MHISP_R}
                        WHEN {vars.MHISP_R} BETWEEN 4 AND 5 THEN 4
                        WHEN {vars.MHISP_R} = 9 THEN 5
                    END
                WHEN {vars.MHISPX} IS NOT NULL THEN
                    CASE
                        WHEN {vars.MHISPX} IN (0, 1, 2, 3) THEN {vars.MHISPX}
                        WHEN {vars.MHISPX} BETWEEN 4 AND 6 THEN 4
                        WHEN {vars.MHISPX} = 9 THEN 5
                    END
                WHEN {vars.UMHISP} IS NOT NULL THEN
                    CASE
                        WHEN {vars.UMHISP} IN (0, 1, 2, 3) THEN {vars.UMHISP}
                        WHEN {vars.UMHISP} BETWEEN 4 AND 5 THEN 4
                        WHEN {vars.UMHISP} = 9 THEN 5
                    END
                WHEN {vars.ORRACEM} IS NOT NULL THEN
                    CASE
                        WHEN {vars.ORRACEM} IN (1, 2, 3) THEN {vars.ORRACEM}
                        WHEN {vars.ORRACEM} BETWEEN 6 AND 8 THEN 0
                        WHEN {vars.ORRACEM} BETWEEN 4 AND 5 THEN 4
                        WHEN {vars.ORRACEM} = 9 THEN 5
                    END
                ELSE NULL
            END
            """
        )

        print("Setting mracehisp_c...")

        con.execute(
            """
            UPDATE us_births
            SET mracehisp_c = CASE
                WHEN mhisp_c BETWEEN 1 AND 4 THEN 5
                WHEN mhisp_c = 5 THEN NULL
                ELSE mrace_c
            END
            """
        )

        print("Reading us-births-estimated-prevalence-maternal-age-1989-2018.csv")

        prev_est_age_df = pd.read_csv(
            "./us-births-estimated-prevalence-maternal-age-1989-2018.csv"
        ).convert_dtypes()

        con.execute(
            """
            CREATE TABLE us_births_est_prevalence_age AS
            SELECT * FROM prev_est_age_df
            """
        )

        print("Setting p_ds_lb_wt_mage...")

        con.execute(
            """
            UPDATE us_births AS b
            SET p_ds_lb_wt_mage =
                    CASE
                        WHEN b.mage_c < 35 THEN e.p_ds_lb_wt_lt35_sv
                        ELSE e.p_ds_lb_wt_gte35_sv
                        END FROM us_births_est_prevalence_age AS e
            WHERE b.year = e.year;
            """
        )

        print("Reading us-births-reduction-rates-1989-2024.csv")

        reduction_df = pd.read_csv(
            "./us-births-reduction-rates-1989-2024.csv"
        ).convert_dtypes()

        print("Creating table reduction_rate_year")

        con.execute(
            """
            CREATE TABLE reduction_rate_year AS
            SELECT * FROM reduction_df
            """
        )

        # set reduction rates
        print("Setting p_ds_lb_wt_mage_reduc")

        con.execute(
            """
            UPDATE us_births AS b
            SET p_ds_lb_wt_mage_reduc = b.p_ds_lb_nt * (1 - r.reduction)
            FROM reduction_rate_year AS r
            WHERE b.year = r.year;
            """
        )

        print("Reading us-births-ds-rec-weights.csv")

        weights_df = pd.read_csv("./us-births-ds-rec-weights.csv").convert_dtypes()

        print("Creating table ds_rec_weights")

        con.execute(
            """
            CREATE TABLE ds_rec_weights AS
            SELECT * FROM weights_df
            """
        )

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN ds_case_weight DOUBLE
            """
        )

        print("Setting ds_rec_weight")

        con.execute(
            """
            UPDATE us_births AS b
            SET ds_case_weight =
                    CASE
                        WHEN b.down_ind = 1 AND b.mracehisp_c = 1 THEN w.nhw
                        WHEN b.down_ind = 1 AND b.mracehisp_c = 2 THEN w.nhb
                        WHEN b.down_ind = 1 AND b.mracehisp_c = 3 THEN w.ai_an
                        WHEN b.down_ind = 1 AND b.mracehisp_c = 4 THEN w.as_pi
                        WHEN b.down_ind = 1 AND b.mracehisp_c = 5 THEN w.his
                        WHEN b.down_ind = 1 THEN w.total
                        ELSE 0
                        END
            FROM ds_rec_weights AS w
            WHERE b.year = w.year;
            """
        )

    finally:

        print("Closing connection...")

        con.close()

    # copy to compress files

    out_db.unlink(missing_ok=True)

    print("Copying from temp_db to db...")

    duckdb.execute(
        f"""
        ATTACH '{out_db_temp.as_posix()}' AS temp_db;
        ATTACH '{out_db.as_posix()}' AS db;
        COPY FROM DATABASE temp_db TO db;
        DETACH temp_db;
        DETACH db;
        """
    )

    print("Copying from db to temp_db...")

    out_db_temp.unlink(missing_ok=True)

    # copy out_db file to out_db_temp overwriting
    shutil.copy2(out_db.as_posix(), out_db_temp.as_posix())

if __name__ == "__main__":
    combine_all()
