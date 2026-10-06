from transform import load_all_races
from load import create_table, insert_results
from extract import fetch_multiple_seasons
import sqlite3
if __name__ == "__main__":
    fetch_multiple_seasons(range(2021, 2027))
    all_results = load_all_races()
    print(len(all_results))
    conn = sqlite3.connect("f1.db")
    create_table(conn)
    insert_results(conn, all_results)

