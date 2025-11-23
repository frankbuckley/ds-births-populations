import pathlib
import pandas as pd
import duckdb
from variables import Variables as vars


def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_db_temp = src_dir / "us_births_temp.db"
    out_db = src_dir / "us_births.db"

    con = duckdb.connect(out_db_temp.as_posix())

    print("--------------------------------------------------------------")
    print(f"Preparing DuckDB '{out_db_temp}'...")
    print("--------------------------------------------------------------")

    try:
        print(f"Altering columns {vars.DATAYEAR}...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.DATAYEAR} TYPE USMALLINT;
            """
        )

        print(f"Altering columns {vars.BIRYR}...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.BIRYR} TYPE USMALLINT;
            """
        )

        print(f"Altering columns {vars.DOB_YY}...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.DOB_YY} TYPE USMALLINT;
            """
        )

        print(f"Altering columns {vars.DOB_MM}...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.DOB_MM} TYPE UTINYINT;
            """
        )

        print(f"Altering columns {vars.DOB_WK}...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.DOB_WK} TYPE UTINYINT;
            """
        )

        print("Altering columns 2...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ALTER {vars.OSTATE} TYPE VARCHAR
                ALTER {vars.XOSTATE} TYPE VARCHAR
                ALTER {vars.OCNTYFIPS} TYPE USMALLINT
                ALTER {vars.OCNTYPOP} TYPE UTINYINT
                ALTER {vars.BFACIL} TYPE UTINYINT
                ALTER {vars.F_BFACIL} TYPE UTINYINT
                ALTER {vars.UMAGERPT} TYPE UTINYINT
                ALTER {vars.MAGE_IMPFLG} TYPE UTINYINT
                ALTER {vars.MAGE_REPFLG} TYPE UTINYINT
                ALTER {vars.MAGER} TYPE UTINYINT
                ALTER {vars.DMAGE} TYPE UTINYINT
                ALTER {vars.DMAGERPT} TYPE UTINYINT
                ALTER {vars.MAGER41} TYPE UTINYINT
                ALTER {vars.MAGER14} TYPE UTINYINT
                ALTER {vars.MAGER9} TYPE UTINYINT
                ALTER {vars.MAGE36} TYPE UTINYINT
                ALTER {vars.MAGER12} TYPE UTINYINT
                ALTER {vars.MAGER8} TYPE UTINYINT
                ALTER {vars.UMBSTATE} TYPE VARCHAR
                ALTER {vars.MBSTATE_REC} TYPE UTINYINT
                ALTER {vars.XMRSTATE} TYPE VARCHAR
                ALTER {vars.MRSTATE} TYPE VARCHAR
                ALTER {vars.RCNTY_POP} TYPE VARCHAR
                ALTER {vars.RCITY_POP} TYPE VARCHAR
                ALTER {vars.METRORES} TYPE VARCHAR
                ALTER {vars.RESTATUS} TYPE UTINYINT
                ALTER {vars.MBRACE} TYPE UTINYINT
                ALTER {vars.MRACE} TYPE UTINYINT
                ALTER {vars.MRACEREC} TYPE UTINYINT
                ALTER {vars.MRACE31} TYPE UTINYINT
                ALTER {vars.MRACE6} TYPE UTINYINT
                ALTER {vars.MRACE15} TYPE UTINYINT
                ALTER {vars.MRACEIMP} TYPE UTINYINT
                ALTER {vars.ORMOTH} TYPE UTINYINT
                ALTER {vars.ORRACEM} TYPE UTINYINT
                ALTER {vars.UMHISP} TYPE UTINYINT
                ALTER {vars.MHISPX} TYPE UTINYINT
                ALTER {vars.MHISP_R} TYPE UTINYINT
                ALTER {vars.F_MHISP} TYPE UTINYINT
                ALTER {vars.MRACEHISP} TYPE UTINYINT
                ALTER {vars.MAR} TYPE UTINYINT
                ALTER {vars.MAR_IMP} TYPE VARCHAR
                ALTER {vars.MAR_P} TYPE VARCHAR
                ALTER {vars.DMAR} TYPE VARCHAR
                ALTER {vars.F_MAR_P} TYPE UTINYINT
                ALTER {vars.DMEDUC} TYPE UTINYINT
                ALTER {vars.MEDUC} TYPE UTINYINT
                ALTER {vars.UMEDUC} TYPE UTINYINT
                ALTER {vars.MEDUC6} TYPE UTINYINT
                ALTER {vars.MEDUC_REC} TYPE UTINYINT
                ALTER {vars.MPLBIR} TYPE UTINYINT
                ALTER {vars.F_MEDUC} TYPE UTINYINT
                ALTER {vars.DFAGE} TYPE UTINYINT
                ALTER {vars.DFAGERPT} TYPE UTINYINT
                ALTER {vars.FAGE11} TYPE UTINYINT
                ALTER {vars.FAGERPT} TYPE UTINYINT
                ALTER {vars.UFAGECOMB} TYPE UTINYINT
                ALTER {vars.FAGERPT_FLG} TYPE VARCHAR
                ALTER {vars.FAGECOMB} TYPE UTINYINT
                ALTER {vars.FAGEREC11} TYPE UTINYINT
                ALTER {vars.FBRACE} TYPE UTINYINT
                ALTER {vars.ORFATH} TYPE UTINYINT
                ALTER {vars.ORRACEF} TYPE UTINYINT
                ALTER {vars.FRACE} TYPE UTINYINT
                ALTER {vars.FRACEIMP} TYPE UTINYINT
                ALTER {vars.FRACEREC} TYPE UTINYINT
                ALTER {vars.UFHISP} TYPE UTINYINT
                ALTER {vars.FRACEHISP} TYPE UTINYINT
                ALTER {vars.FRACE31} TYPE UTINYINT
                ALTER {vars.FRACE6} TYPE UTINYINT
                ALTER {vars.FRACE15} TYPE UTINYINT
                ALTER {vars.FHISPX} TYPE UTINYINT
                ALTER {vars.FHISP_R} TYPE UTINYINT
                ALTER {vars.F_FHISP} TYPE UTINYINT
                ALTER {vars.FEDUC} TYPE UTINYINT
                ALTER {vars.PRIORLIVE} TYPE UTINYINT
                ALTER {vars.PRIORDEAD} TYPE UTINYINT
                ALTER {vars.PRIORTERM} TYPE UTINYINT
                ALTER {vars.LBO} TYPE UTINYINT
                ALTER {vars.LBO_REC} TYPE UTINYINT
                ALTER {vars.TBO} TYPE UTINYINT
                ALTER {vars.TBO_REC} TYPE UTINYINT
                ALTER {vars.ILLB_R} TYPE UTINYINT
                ALTER {vars.ILLB_R11} TYPE UTINYINT
                ALTER {vars.ILLB_R} TYPE UTINYINT
                ALTER {vars.DLLB_MM} TYPE UTINYINT
                ALTER {vars.DLLB_YY} TYPE USMALLINT
                ALTER {vars.PRECARE} TYPE UTINYINT
                ALTER {vars.AMNIO} TYPE UTINYINT
                ALTER {vars.PAY} TYPE UTINYINT
                ALTER {vars.PAY_REC} TYPE UTINYINT
                ALTER {vars.F_PAY} TYPE UTINYINT
                ALTER {vars.F_PAY_REC} TYPE UTINYINT
                ALTER {vars.APGAR5} TYPE UTINYINT
                ALTER {vars.APGAR5R} TYPE UTINYINT
                ALTER {vars.F_APGAR5} TYPE UTINYINT
                ALTER {vars.APGAR10} TYPE UTINYINT
                ALTER {vars.DPLURAL} TYPE UTINYINT
                ALTER {vars.IMP_PLURAL} TYPE UTINYINT
                ALTER {vars.SETORDER_R} TYPE UTINYINT
                ALTER {vars.SEX} TYPE VARCHAR
                ALTER {vars.COMBGEST} TYPE UTINYINT
                ALTER {vars.GESTREC10} TYPE UTINYINT
                ALTER {vars.LMPUSED} TYPE UTINYINT
                ALTER {vars.OEGEST_COMB} TYPE UTINYINT
                ALTER {vars.OEGEST_R10} TYPE UTINYINT
                ALTER {vars.OEGEST_R3} TYPE UTINYINT
                ALTER {vars.DBWT} TYPE UTINYINT
                ALTER {vars.BWTR12} TYPE UTINYINT
                ALTER {vars.BWTR4} TYPE UTINYINT
                ALTER {vars.DWGT_R} TYPE UTINYINT
                ALTER {vars.F_DWGT} TYPE UTINYINT
                ALTER {vars.AB_AVEN1} TYPE VARCHAR
                ALTER {vars.AB_AVEN6} TYPE VARCHAR
                ALTER {vars.AB_NICU} TYPE VARCHAR
                ALTER {vars.AB_SURF} TYPE VARCHAR
                ALTER {vars.AB_ANTI} TYPE VARCHAR
                ALTER {vars.AB_SEIZ} TYPE VARCHAR
                ALTER {vars.NO_ABNORM} TYPE UTINYINT
                ALTER {vars.CONGENIT} TYPE VARCHAR
                ALTER {vars.CA_ANEN} TYPE VARCHAR
                ALTER {vars.CA_MNSB} TYPE VARCHAR
                ALTER {vars.CA_CCHD} TYPE VARCHAR
                ALTER {vars.CA_ANEN} TYPE VARCHAR
                ALTER {vars.CA_MNSB} TYPE VARCHAR
                ALTER {vars.CA_CCHD} TYPE VARCHAR
                ALTER {vars.CA_CDH} TYPE VARCHAR
                ALTER {vars.CA_OMPH} TYPE VARCHAR
                ALTER {vars.CA_GAST} TYPE VARCHAR
                ALTER {vars.F_CA_ANEN} TYPE VARCHAR
                ALTER {vars.F_CA_MENIN} TYPE VARCHAR
                ALTER {vars.F_CA_HEART} TYPE VARCHAR
                ALTER {vars.F_CA_HERNIA} TYPE VARCHAR
                ALTER {vars.F_CA_OMPHA} TYPE VARCHAR

                ALTER {vars.ATTEND} TYPE UTINYINT


            """
        )

        print("Adding columns...")

        con.execute(
            f"""
            ALTER TABLE us_births
                ADD COLUMN {vars.YEAR} USMALLINT
                ADD COLUMN {vars.MAGE_C} UTINYINT
                ADD COLUMN {vars.MRACE_C} UTINYINT
                ADD COLUMN {vars.MHISP_C} UTINYINT
                ADD COLUMN {vars.MRACEHISP_C} UTINYINT
                ADD COLUMN {vars.DOWN_IND} UTINYINT
                ADD COLUMN {vars.CA_DOWN_C} VARCHAR
                ADD COLUMN {vars.P_DS_LB_WT} DOUBLE
                ADD COLUMN {vars.P_DS_LB_NT} DOUBLE
                ADD COLUMN {vars.P_DS_LB_WT_MAGE} DOUBLE
                ADD COLUMN {vars.P_DS_LB_NT_MAGE} DOUBLE
                ADD COLUMN {vars.P_DS_LB_WT_ETHN} DOUBLE
                ADD COLUMN {vars.P_DS_LB_NT_ETHN} DOUBLE
                ADD COLUMN {vars.P_DS_LB_WT_MAGE_REDUC} DOUBLE
            """
        )

        print("Setting mrace_c...")

        con.execute(
            """
            UPDATE us_births
            SET mrace_c = CASE
                WHEN mrace15 IS NOT NULL AND (year < 2014 OR year > 2019) THEN
                    CASE
                        WHEN mrace15 IN(1, 2, 3) THEN mrace15
                        WHEN mrace15 BETWEEN 4 AND 14 THEN 4
                    END
                WHEN mracerec IS NOT NULL AND (year < 2014 OR year > 2019) THEN
                    CASE
                        WHEN mracerec IN(1, 2, 3, 4) THEN mracerec
                    END
                WHEN mbrace IS NOT NULL THEN
                    CASE
                        WHEN mbrace IN(1, 2, 3, 4) THEN mbrace
                    END
                WHEN mrace IS NOT NULL THEN
                    CASE
                        WHEN mrace IN(1, 2, 3) THEN mrace
                        WHEN mrace BETWEEN 4 AND 78 THEN 4
                    END
                ELSE NULL
            END
            """
        )

        print("Setting mhisp_c...")

        con.execute(
            """
            UPDATE us_births
            SET mhisp_c = CASE
                WHEN mhisp_r IS NOT NULL THEN
                    CASE
                        WHEN mhisp_r IN (0, 1, 2, 3) THEN mhisp_r
                        WHEN mhisp_r BETWEEN 4 AND 5 THEN 4
                        WHEN mhisp_r = 9 THEN 5
                        END
                WHEN mhispx IS NOT NULL THEN
                    CASE
                        WHEN mhispx IN (0, 1, 2, 3) THEN mhispx
                        WHEN mhispx BETWEEN 4 AND 6 THEN 4
                        WHEN mhispx = 9 THEN 5
                        END
                WHEN umhisp IS NOT NULL THEN
                    CASE
                        WHEN umhisp IN (0, 1, 2, 3) THEN umhisp
                        WHEN umhisp BETWEEN 4 AND 5 THEN 4
                        WHEN umhisp = 9 THEN 5
                        END
                WHEN orracem IS NOT NULL THEN
                    CASE
                        WHEN orracem IN (1, 2, 3) THEN orracem
                        WHEN orracem BETWEEN 6 AND 8 THEN 0
                        WHEN orracem BETWEEN 4 AND 5 THEN 4
                        WHEN orracem = 9 THEN 5
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
        con.close()


if __name__ == "__main__":
    combine_all()
