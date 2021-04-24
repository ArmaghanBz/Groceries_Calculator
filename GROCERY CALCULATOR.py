import os
items=int(input("How many items you bought? "))
i = 1
price = 0
price_i = 0
while i <= items:
    print("Item ", i ,":")
    price_i=float(input(" enter the price of item: "))
    price += price_i
    i = i + 1
change = float(input("How much money you gave? "))
total= price
money_back = change - total
print("The total price is: ", total)
print ("Your Change: ", money_back)

os.system("pause")