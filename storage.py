import json
import os

from config import DATA_DIR, PLANTS_FILE, CARE_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    for file_path in [PLANTS_FILE, CARE_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)


def load_json(file_path):
    initialize_storage()

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_json(file_path, data):
    initialize_storage()

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_plants():
    return load_json(PLANTS_FILE)


def save_plants(plants):
    save_json(PLANTS_FILE, plants)


def load_care_records():
    return load_json(CARE_FILE)


def save_care_records(records):
    save_json(CARE_FILE, records)
