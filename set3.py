rows = 5
seats = 10

cinema = []

# Create seating arrangement
for i in range(rows):
    row = []

    for j in range(seats):
        row.append(0)

    cinema.append(row)


total_revenue = 0

# Display initial seating arrangement
print("----- SEATING ARRANGEMENT -----")

for i in range(rows):
    for j in range(seats):
        print(cinema[i][j], end=" ")

    print()


# Booking seats
while True:

    row = int(input("\nEnter row number (1-5): "))
    seat = int(input("Enter seat number (1-10): "))

    if row < 1 or row > 5:
        print("Invalid row number!")

    elif seat < 1 or seat > 10:
        print("Invalid seat number!")

    elif cinema[row - 1][seat - 1] == 1:
        print("Seat is already booked!")

    else:
        cinema[row - 1][seat - 1] = 1

        # Calculate ticket price
        if row <= 2:
            price = 150
        elif row <= 4:
            price = 200
        else:
            price = 250

        total_revenue = total_revenue + price

        print("Seat booked successfully!")
        print("Ticket Price: ₹", price)

    choice = input("\nDo you want to book another seat? (y/n): ")

    if choice != "y":
        break


# Count booked and available seats
booked = 0
available = 0

for i in range(rows):
    for j in range(seats):

        if cinema[i][j] == 1:
            booked = booked + 1
        else:
            available = available + 1


# Find row with maximum booked seats
max_booked = 0
max_row = 0

for i in range(rows):

    count = 0

    for j in range(seats):

        if cinema[i][j] == 1:
            count = count + 1

    if count > max_booked:
        max_booked = count
        max_row = i + 1


# Booking summary
print("\n----- BOOKING SUMMARY -----")

print("Total booked seats:", booked)
print("Total available seats:", available)
print("Total revenue: ₹", total_revenue)

if max_booked > 0:
    print("Row with maximum booked seats:", max_row)
    print("Booked seats in that row:", max_booked)
else:
    print("No seats have been booked.")


# Final seating arrangement
print("\n----- FINAL SEATING ARRANGEMENT -----")

for i in range(rows):

    print("Row", i + 1, ":", end=" ")

    for j in range(seats):
        print(cinema[i][j], end=" ")

    print()