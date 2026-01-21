import os

FILE_NAME = "bookings.txt"

def add_booking():
    booking_id = input("Enter Booking ID: ")
    name = input("Enter Customer Name: ")
    date = input("Enter Booking Date (DD-MM-YYYY): ")
    time = input("Enter Time Slot: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{booking_id},{name},{date},{time}\n")

    print("✅ Booking added successfully!")

def view_bookings():
    if not os.path.exists(FILE_NAME):
        print("No bookings found.")
        return

    with open(FILE_NAME, "r") as file:
        print("\n--- All Bookings ---")
        for line in file:
            booking_id, name, date, time = line.strip().split(",")
            print(f"ID: {booking_id}, Name: {name}, Date: {date}, Time: {time}")

def search_booking():
    search_id = input("Enter Booking ID to search: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No bookings found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            booking_id, name, date, time = line.strip().split(",")
            if booking_id == search_id:
                print(f"✅ Booking Found → {name}, {date}, {time}")
                found = True
                break

    if not found:
        print("❌ Booking not found.")

def cancel_booking():
    cancel_id = input("Enter Booking ID to cancel: ")
    updated_lines = []
    found = False

    if not os.path.exists(FILE_NAME):
        print("No bookings found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            if not line.startswith(cancel_id + ","):
                updated_lines.append(line)
            else:
                found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)

    if found:
        print("✅ Booking cancelled successfully!")
    else:
        print("❌ Booking ID not found.")

def main():
    while True:
        print("\n--- Booking Management System ---")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_booking()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            search_booking()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("👋 Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
