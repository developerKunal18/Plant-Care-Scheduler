from storage import load_plants, save_plants
from utils import (
    get_next_id,
    input_required,
    input_integer,
    display_plant
)


def add_plant():
    plants = load_plants()

    print("\n--- ADD PLANT ---")

    name = input_required("Enter plant name: ")
    plant_type = input_required("Enter plant type: ")
    location = input_required("Enter plant location: ")

    watering_interval = input_integer(
        "Watering interval in days: "
    )

    fertilizing_interval = input_integer(
        "Fertilizing interval in days: "
    )

    plant = {
        "id": get_next_id(plants),
        "name": name,
        "plant_type": plant_type,
        "location": location,
        "watering_interval": watering_interval,
        "fertilizing_interval": fertilizing_interval
    }

    plants.append(plant)
    save_plants(plants)

    print("\nPlant added successfully!")


def view_plants():
    plants = load_plants()

    if not plants:
        print("\nNo plants registered.")
        return

    print("\n--- REGISTERED PLANTS ---")

    for plant in plants:
        display_plant(plant)


def search_plants():
    plants = load_plants()

    keyword = input_required(
        "Enter plant name to search: "
    ).lower()

    results = [
        plant for plant in plants
        if keyword in plant["name"].lower()
    ]

    if not results:
        print("\nNo matching plants found.")
        return

    for plant in results:
        display_plant(plant)
