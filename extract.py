import json, time, requests
from pathlib import Path

BASE_URL = "https://api.jolpi.ca/ergast/f1"
RAW_DATA_DIR = Path("data/raw")

def fetch_race_results(season: int, round_number: int) -> dict | None:
    filepath = RAW_DATA_DIR / f"{season}_round_{round_number}.json"
    if filepath.exists():
        print(f"  Already have season {season} round {round_number}, loading from disk")
        with open(filepath, "r") as f:
            return json.load(f)
    url = f"{BASE_URL}/{season}/{round_number}/results.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        time.sleep(0.5)
    except requests.RequestException as e:
        print(f"  Failed to fetch season {season} round {round_number}: {e}")
        return None
    return response.json()

def save_raw_json(data: dict, season: int, round_number: int) -> Path:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    filepath = RAW_DATA_DIR / f"{season}_round_{round_number}.json"
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    return filepath

def fetch_season(season: int, max_rounds: int = 24) -> list[Path]:
    saved_files = []
    for round_number in range(1, max_rounds + 1):
        print(f"Fetching {season} round {round_number}...")
        data = fetch_race_results(season, round_number)
        races = data["MRData"]["RaceTable"]["Races"] if data else []
        if not races:
            print(f"No more races found after round {round_number - 1}. Stopping.")
            break
        filepath = save_raw_json(data, season, round_number)
        saved_files.append(filepath)
    return saved_files

def fetch_multiple_seasons(seasons):
    for year in seasons:
        fetch_season(year)
