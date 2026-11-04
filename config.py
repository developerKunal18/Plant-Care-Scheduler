import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PLANTS_FILE = os.path.join(DATA_DIR, "plants.json")
CARE_FILE = os.path.join(DATA_DIR, "care_records.json")

CARE_TYPES = ["Watering", "Fertilizing", "Pruning", "Other"]
