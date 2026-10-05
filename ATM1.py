balance = float(input("Enter initial balance: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Amount deposited")
        else:
            print("Invalid deposit amount")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0:
            if amount <= balance:
                balance = balance - amount
                print("Amount withdrawn")

                if balance < 500:
                    print("Warning: Balance is below 500")
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")