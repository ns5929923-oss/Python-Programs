menu = {
    1: ("Pizza", 250),
    2: ("Burger", 150),
    3: ("Pasta", 200),
    4: ("Sandwich", 120),
    5: ("Biryani", 300),
    6: ("Dosa", 100),
    7: ("Noodles", 180),
    8: ("Ice Cream", 80)
}

total_revenue = 0
highest_bill = 0

print("----- RESTAURANT MENU -----")

for number, item in menu.items():
    print(number, item[0], "₹", item[1])

customers = int(input("\nEnter number of customers: "))

for c in range(customers):
    print("\n----- Customer", c + 1, "-----")

    total = 0
    different_items = 0

    while True:
        item_no = int(input("Enter item number (1-8): "))
        quantity = int(input("Enter quantity: "))

        if item_no in menu:
            name = menu[item_no][0]
            price = menu[item_no][1]

            amount = price * quantity
            total = total + amount
            different_items = different_items + 1

            print(name, "x", quantity, "= ₹", amount)
        else:
            print("Invalid item number!")

        choice = input("Do you want to order another item? (y/n): ")

        if choice != "y":
            break

    if total < 500:
        discount = 0
    elif total < 1000:
        discount = total * 5 / 100
    elif total < 2000:
        discount = total * 10 / 100
    else:
        discount = total * 15 / 100

    if different_items >= 4:
        extra_discount = total * 5 / 100
    else:
        extra_discount = 0

    final_bill = total - discount - extra_discount

    print("\nSubtotal: ₹", total)
    print("Discount: ₹", discount)
    print("Additional Discount: ₹", extra_discount)
    print("Final Bill: ₹", final_bill)

    total_revenue = total_revenue + final_bill

    if final_bill > highest_bill:
        highest_bill = final_bill

print("\n----- RESTAURANT SUMMARY -----")
print("Highest Bill: ₹", highest_bill)
print("Total Restaurant Revenue: ₹", total_revenue)