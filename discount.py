product1 = int(input("enter your product: "))
product2 = int(input("enter your product: "))
product3 = int(input("enter your product: "))
product4 = int(input("enter your product: "))

total= product1 + product2 + product3 + product4
print("you total is:",total)

if total > 2000:
    discount = total * 20 / 100
    print("You got 20% discount")

elif total > 1500:
    discount = total * 15 / 100
    print("You got 15% discount")

elif total > 1000:
    discount = total * 10 / 100
    print("You got 10% discount")
    
else:
    discount = 0
    print("No discount!!")
    
final_amount = total - discount

print("Discount amount:", discount)
print("Amount after discount:", final_amount)    


