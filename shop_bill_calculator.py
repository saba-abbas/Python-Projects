item1 = input("Enter first item name: ")
item2 = input("Enter second item name: ")
item3 = input("Enter third item name: ")

price1 = float(input(f"Enter price of {item1}: "))
price2 = float(input(f"Enter price of {item2}: "))
price3 = float(input(f"Enter price of {item3}: "))

quantity1 = int(input(f"Enter quantity of {item1}: "))
quantity2 = int(input(f"Enter quantity of {item2}: "))
quantity3 = int(input(f"Enter quantity of {item3}: "))

total = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

print(f"Your total bill is: {total}")

if total >= 5000:
    discount = total * 0.10
    final = total - discount
    print(f"You get 10% discount! Final bill: {final}")
elif total >= 3000:
    discount = total * 0.05
    final = total - discount
    print(f"You get 5% discount! Final bill: {final}")
else:
    print(f"No discount. Your total bill is: {total}")
