# foodCart is an empty list
foodCart = []

foodItem = input("Enter a Food Item of your Choice")
foodCart.append(foodItem)

foodItem = input("Enter another Food Item of your Choice")
foodCart.append(foodItem)

print(foodCart)

foodCart.append("Manchurian")

# extend function of list will help us to add more than 1 element in the end of list :)
# and the same list will be modified with new data added in it
foodCart.extend(["Veg Soup", "Breadsticks"])

print(foodCart)

foodCart.insert(1, "Pizza")  # We are adding a new element on index 1

print(foodCart)
