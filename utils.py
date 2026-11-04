from datetime import datetime


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(message, minimum=1):
    while True:
        try:
            value = int(input(message))

            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value

        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def display_plant(plant):
    print("-" * 60)
    print(f"ID                : {plant['id']}")
    print(f"Plant Name        : {plant['name']}")
    print(f"Plant Type        : {plant['plant_type']}")
    print(f"Location          : {plant['location']}")
    print(f"Watering Interval : {plant['watering_interval']} days")
    print(f"Fertilizing Cycle : {plant['fertilizing_interval']} days")


def display_care_record(record):
    print("-" * 60)
    print(f"Care ID      : {record['id']}")
    print(f"Plant Name   : {record['plant_name']}")
    print(f"Care Type    : {record['care_type']}")
    print(f"Due Date     : {record['due_date']}")
    print(f"Status       : {record['status']}")
