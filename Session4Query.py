priceList = []

choice = "yes"
while choice == "yes":
    price = int(input("Enter Price:"))
    priceList.append(price)
    choice = input("Would you like to add more(yes/no)")

print(priceList)

sum = 0

for price in priceList:
    sum = sum + price

print(">> sum is:", sum)

numbers = [23, 54, 78, 90, 76]
print(len(numbers))

