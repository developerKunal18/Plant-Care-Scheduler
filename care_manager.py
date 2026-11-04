from datetime import date

from storage import (
    load_plants,
    load_care_records,
    save_care_records
)

from config import CARE_TYPES

from utils import (
    get_next_id,
    input_required,
    input_date,
    display_care_record
)


def schedule_care():
    plants = load_plants()

    if not plants:
        print("Please add a plant first.")
        return

    print("\n--- SELECT PLANT ---")

    for plant in plants:
        print(f"{plant['id']}. {plant['name']}")

    try:
        plant_id = int(input("Enter plant ID: "))
    except ValueError:
        print("Enter a valid plant ID.")
        return

    plant = next(
        (item for item in plants if item["id"] == plant_id),
        None
    )

    if not plant:
        print("Plant not found.")
        return

    print("\nCare Types:")

    for index, care_type in enumerate(CARE_TYPES, start=1):
        print(f"{index}. {care_type}")

    try:
        care_choice = int(input("Select care type: "))
    except ValueError:
        print("Enter a valid choice.")
        return

    if care_choice < 1 or care_choice > len(CARE_TYPES):
        print("Invalid care type.")
        return

    care_type = CARE_TYPES[care_choice - 1]
    due_date = input_date("Enter due date (YYYY-MM-DD): ")

    records = load_care_records()

    record = {
        "id": get_next_id(records),
        "plant_id": plant["id"],
        "plant_name": plant["name"],
        "care_type": care_type,
        "due_date": due_date,
        "status": "Pending",
        "completed_date": None
    }

    records.append(record)
    save_care_records(records)

    print("\nCare activity scheduled successfully!")


def view_care_records():
    records = load_care_records()

    if not records:
        print("\nNo care records found.")
        return

    print("\n--- CARE SCHEDULE ---")

    for record in records:
        display_care_record(record)


def complete_care():
    records = load_care_records()

    try:
        record_id = int(input("Enter care record ID: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    record = next(
        (item for item in records if item["id"] == record_id),
        None
    )

    if not record:
        print("Care record not found.")
        return

    if record["status"] == "Completed":
        print("This activity is already completed.")
        return

    record["status"] = "Completed"
    record["completed_date"] = date.today().isoformat()

    save_care_records(records)

    print("Care activity marked as completed!")


def view_due_care():
    records = load_care_records()
    today = date.today()

    due_records = [
        record for record in records
        if record["status"] == "Pending"
        and date.fromisoformat(record["due_date"]) <= today
    ]

    if not due_records:
        print("\nNo care activities are due today.")
        return

    print("\n--- DUE AND OVERDUE CARE ---")

    for record in due_records:
        display_care_record(record)
