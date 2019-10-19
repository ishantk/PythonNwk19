"""

    Restaurant HAS-A FoodItem
    1 to many Mapping
    1 Restaurant Has Many FoodItems

"""

class FoodItem:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    def showFoodItem(self):
        print("------------------------------------")
        print(self.name, " | ", self.price, " | ", self.rating)
        print("------------------------------------")
        print()


class Restaurant:

    def __init__(self, name, phone, address, rating, pricePerPerson, items):
        self.restaurantName = name
        self.phone = phone
        self.address = address
        self.rating = rating
        self.pricePerPerson = pricePerPerson
        self.items = items # 1 to many mapping (HAS-A Relation)

    def showRestaurantDetails(self):
        print("===", self.restaurantName, "====")
        print(">>", self.address, " | ", self.phone, " | ", self.rating)

        # Iterating in a List of FoodItem Objects
        for item in self.items:
            item.showFoodItem()


item1 = FoodItem("Poori Channa", 105, 4.5)
item2 = FoodItem("Dal Kachori", 87, 4.8)
item3 = FoodItem("Samosa", 18, 4.0)
# print(">> item1 is:",item1) # 0x102242e80

# List of Objects :)
items = [item1, item2, item3]

r1 = Restaurant("Gopal Sweets", "+91 99999 88888", "Redwood Shores", 4.5, 200, items)
# print(">> r1 is:", r1) # 0x102a22e80

r1.showRestaurantDetails()



