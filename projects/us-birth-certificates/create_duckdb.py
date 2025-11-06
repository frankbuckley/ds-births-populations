import pathlib
import duckdb


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

    finally:
        con.close()


if __name__ == "__main__":
    combine_all()
