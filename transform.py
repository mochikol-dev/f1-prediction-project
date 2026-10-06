import json
from pathlib import Path

def get_sorted_files():
    raw_dir = Path("data/raw")
    files = list(raw_dir.glob("*.json"))

    def season_round_key(filepath):
        pieces = filepath.stem.split("_")
        return (int(pieces[0]), int(pieces[2]))

    sorted_files = sorted(files, key=season_round_key)
    return sorted_files

def load_all_races():
    files = get_sorted_files()
    payload = []
    for f in files:
        payload.extend(load_race_files(f))
    return payload

def load_race_files(filepath):
    with open(filepath, "r") as f:
        metadata = json.load(f)
        race = metadata["MRData"]["RaceTable"]["Races"][0]
        results = race["Results"]
        data = []
        for x in results:
            driver_result = {
                "round": race["round"],
                "season": race["season"],
                "raceName": race["raceName"],
                "driver_id": x["Driver"]["driverId"],
                "driver": x["Driver"]["familyName"],
                "team": x["Constructor"]["name"],
                "position": int(x["position"]),
                "points": float(x["points"]),
                "grid": int(x["grid"]),
                "status": x["status"]
                } 
            data.append(driver_result)
        print(data)
    return data