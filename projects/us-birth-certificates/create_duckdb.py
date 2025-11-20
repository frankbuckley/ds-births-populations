import pathlib
import pandas as pd
import duckdb
from variables import Variables as vars

def combine_all() -> None:
    src_dir = pathlib.Path("data")
    out_parquet = src_dir / "us_births.parquet"
    out_db = src_dir / "us_births.db"

    out_db.unlink(missing_ok=True)

    con = duckdb.connect(out_db.as_posix())

    print("Importing Parquet file into DuckDB us_births...")

    try:
        con.execute(
            """
            CREATE TABLE us_births AS
            SELECT *
            FROM read_parquet(?)
            """,
            [out_parquet.as_posix()],
        )

        print("Adding mrace_c column...")

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN mrace_c UTINYINT
            """
        )

        print("Adding mhisp_c column")

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN mhisp_c UTINYINT
            """
        )

        print("Adding mracehisp_c column")

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN mracehisp_c UTINYINT
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

        print("Adding p_ds_lb_wt_mage column")

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN p_ds_lb_wt_mage DOUBLE
            """
        )

        print("Adding p_ds_lb_nt_mage column")

        con.execute(
            """
            ALTER TABLE us_births
                ADD COLUMN p_ds_lb_nt_mage DOUBLE
            """
        )

        print("Adding p_ds_lb_wt_ethn column")

        con.execute(
            f"""
            ALTER TABLE us_births
                ADD COLUMN {vars.P_DS_LB_WT_ETHN} DOUBLE
            """
        )

        print("Adding p_ds_lb_nt_ethn column")

        con.execute(
            f"""
            ALTER TABLE us_births
                ADD COLUMN {vars.P_DS_LB_NT_ETHN} DOUBLE
            """
        )

        print("Adding p_ds_lb_wt_mage_reduc column")

        con.execute(
            f"""
            ALTER TABLE us_births
                ADD COLUMN {vars.P_DS_LB_WT_MAGE_REDUC} DOUBLE
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

        print ("Setting ds_rec_weight")

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
