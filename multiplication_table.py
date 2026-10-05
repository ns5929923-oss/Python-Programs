n = int(input("Enter number: "))

for i in range(1, n + 1):

    print("Table of", i)

    for j in range(1, 11):
        print(i * j)

    print()
    
    while True:
    n = int(input("Enter number : "))

    for i in range(1,11):
        print(n, "x",i, "=", n*i)
        
    choice =  input("do you want another table? (yes/no):")
    
    if choice== "no":
        break
