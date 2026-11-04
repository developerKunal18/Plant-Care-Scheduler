from storage import load_plants, load_care_records


def show_report():
    plants = load_plants()
    records = load_care_records()

    total_plants = len(plants)
    total_care_records = len(records)

    pending = sum(
        1 for record in records
        if record["status"] == "Pending"
    )

    completed = sum(
        1 for record in records
        if record["status"] == "Completed"
    )

    watering = sum(
        1 for record in records
        if record["care_type"] == "Watering"
    )

    fertilizing = sum(
        1 for record in records
        if record["care_type"] == "Fertilizing"
    )

    print("\n========== PLANT CARE REPORT ==========")
    print(f"Total Plants       : {total_plants}")
    print(f"Total Care Records : {total_care_records}")
    print(f"Pending Activities : {pending}")
    print(f"Completed          : {completed}")
    print(f"Watering Tasks     : {watering}")
    print(f"Fertilizing Tasks  : {fertilizing}")
    print("======================================")
