floors = 3
rows = 5
spaces = 10

parking = []

for i in range(floors):
    floor = []

    for j in range(rows):
        row = []

        for k in range(spaces):
            row.append(0)

        floor.append(row)

    parking.append(floor)

total_revenue = 0

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        floor = int(input("Enter floor number (1-3): "))
        row = int(input("Enter row number (1-5): "))
        space = int(input("Enter parking space (1-10): "))

        if floor < 1 or floor > 3:
            print("Invalid floor number!")

        elif row < 1 or row > 5:
            print("Invalid row number!")

        elif space < 1 or space > 10:
            print("Invalid parking space!")

        elif parking[floor - 1][row - 1][space - 1] == 1:
            print("Parking space is already occupied!")

        else:
            vehicle = input("Enter vehicle type (two-wheeler/car/SUV): ").lower()
            hours = int(input("Enter parking hours: "))

            if vehicle == "two-wheeler":
                charge = 20 * hours

            elif vehicle == "car":
                charge = 50 * hours

            elif vehicle == "suv":
                charge = 70 * hours

            else:
                print("Invalid vehicle type!")
                continue

            if hours <= 2:
                extra = 0
            elif hours <= 5:
                extra = charge * 10 / 100
            else:
                extra = charge * 20 / 100

            final_charge = charge + extra

            parking[floor - 1][row - 1][space - 1] = 1

            total_revenue = total_revenue + final_charge

            print("Vehicle parked successfully!")
            print("Parking Charge: ₹", final_charge)

    elif choice == 2:
        floor = int(input("Enter floor number (1-3): "))
        row = int(input("Enter row number (1-5): "))
        space = int(input("Enter parking space (1-10): "))

        if floor < 1 or floor > 3:
            print("Invalid floor number!")

        elif row < 1 or row > 5:
            print("Invalid row number!")

        elif space < 1 or space > 10:
            print("Invalid parking space!")

        elif parking[floor - 1][row - 1][space - 1] == 0:
            print("Parking space is already empty!")

        else:
            parking[floor - 1][row - 1][space - 1] = 0
            print("Vehicle removed successfully!")

    elif choice == 3:
        break

    else:
        print("Invalid choice!")


print("\n----- FLOOR OCCUPANCY -----")

highest_occupied = 0
highest_floor = 0
total_occupied = 0
total_available = 0

for i in range(floors):
    occupied = 0
    available = 0

    for j in range(rows):
        for k in range(spaces):

            if parking[i][j][k] == 1:
                occupied = occupied + 1
            else:
                available = available + 1

    print("Floor", i + 1)
    print("Occupied:", occupied)
    print("Available:", available)

    total_occupied = total_occupied + occupied
    total_available = total_available + available

    if occupied > highest_occupied:
        highest_occupied = occupied
        highest_floor = i + 1


print("\n----- FINAL RESULT -----")

print("Total Occupied Spaces:", total_occupied)
print("Total Available Spaces:", total_available)

if highest_occupied > 0:
    print("Floor with Highest Occupancy:", highest_floor)
    print("Occupied Spaces:", highest_occupied)
else:
    print("No vehicles are parked.")

print("Total Parking Revenue: ₹", total_revenue)