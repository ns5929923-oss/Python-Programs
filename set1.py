n = int(input("Enter number of consumers: "))
total_revenue = 0
highest_bill = 0
highest_name = ""
below_100 = 0
from_100_300 = 0
from_301_400 = 0
above_400 = 0
for i in range(n):
    print("\nConsumer", i + 1)
    name = input("Enter consumer name: ")
    units = int(input("Enter units consumed: "))
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + ((units - 100) * 7)
    elif units <= 400:
        bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
    else:
        bill = (100 * 5) + (200 * 7) + (100 * 10) + ((units - 400) * 12)
        bill = bill + 100
    if bill > 5000:
        bill = bill + (bill * 5 / 100)
        print("Consumer Name:", name)
        print("Units Consumed:", units)
        print("Total Bill: ₹", bill)
    if bill > highest_bill:
        highest_bill = bill
        highest_name = name
        total_revenue = total_revenue + bill
    if units < 100:
        below_100 = below_100 + 1
    elif units <= 300:
        from_100_300 = from_100_300 + 1
    elif units <= 400:
        from_301_400 = from_301_400 + 1
    else:
        above_400 = above_400 + 1
print("\n----- FINAL RESULT -----")
print("Consumer with highest bill:", highest_name)
print("Highest Bill: ₹", highest_bill)
print("Total Revenue: ₹", total_revenue)
print("\nConsumption Categories:")
print("Below 100 units:", below_100)
print("100–300 units:", from_100_300)
print("301–400 units:", from_301_400)
print("Above 400 units:", above_400)    