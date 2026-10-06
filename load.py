import sqlite3

def create_table(conn):
    cursor = conn.cursor()
    create_table_sql = """CREATE TABLE IF NOT EXISTS race_results (
            driver_id TEXT,
            driver TEXT,
            team TEXT,
            position INTEGER,
            points INTEGER,
            grid INTEGER,
            status TEXT,
            round INTEGER,
            season INTEGER,
            race_name TEXT,
            UNIQUE(driver_id, round, season))"""
    cursor.execute(create_table_sql)
    conn.commit()
    return conn

def insert_results(conn, results):
    cursor = conn.cursor()
    insert_sql = """INSERT OR IGNORE INTO race_results (driver_id, driver, team, position, points, grid, status, round, season, race_name)
    VALUES (?,?,?,?,?,?,?,?,?,?)"""
    for row in results:
        values=(
            row["driver_id"],row["driver"], row["team"], row["position"],row["points"], row["grid"],row["status"], row["round"], row["season"], row["raceName"] 
        )
        cursor.execute(insert_sql, values)
        conn.commit()
    return conn