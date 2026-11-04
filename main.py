from storage import initialize_storage

from plant_manager import (
    add_plant,
    view_plants,
    search_plants
)

from care_manager import (
    schedule_care,
    view_care_records,
    complete_care,
    view_due_care
)

from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n================================")
        print("       PLANT CARE SCHEDULER")
        print("================================")

        print("1. Add Plant")
        print("2. View Plants")
        print("3. Search Plants")
        print("4. Schedule Care Activity")
        print("5. View Care Schedule")
        print("6. Complete Care Activity")
        print("7. View Due Care Activities")
        print("8. View Reports")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_plant()

        elif choice == "2":
            view_plants()

        elif choice == "3":
            search_plants()

        elif choice == "4":
            schedule_care()

        elif choice == "5":
            view_care_records()

        elif choice == "6":
            complete_care()

        elif choice == "7":
            view_due_care()

        elif choice == "8":
            show_report()

        elif choice == "9":
            print("\nThank you for using Plant Care Scheduler!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
