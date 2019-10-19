"""

    Restaurant HAS-A FoodItem
    1 to 1 Mapping
    1 Restaurant Has 1 FoodItem

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

    def __init__(self, name, phone, address, rating, pricePerPerson, item):
        self.restaurantName = name
        self.phone = phone
        self.address = address
        self.rating = rating
        self.pricePerPerson = pricePerPerson
        self.item = item # 1 to 1 mapping (HAS-A Relation) | Reference Copy
        # print(">> self.item is:", self.item)

    def showRestaurantDetails(self):
        print("===", self.restaurantName, "====")
        print(">>", self.address, " | ", self.phone, " | ", self.rating)

        self.item.showFoodItem()  # To Display the data for FoodItem Object


item1 = FoodItem("Poori Channa", 105, 4.5)
# print(">> item1 is:",item1) # 0x102242e80

r1 = Restaurant("John's Cafe", "+91 99999 88888", "Redwood Shores", 4.5, 200, item1)
# print(">> r1 is:", r1) # 0x102a22e80

r1.showRestaurantDetails()



