"""

    OOPS Principle:

    1. Think of an Object
       FoodItem : name, price, rating

    2. Create its Class

    3. From Class Create a real Object in Memory

"""

class FoodItem:

    # def __init__(self):
    #     self.name = "NA"
    #     self.price = 0
    #     self.rating = 0

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    def showFoodItem(self):
        print("------------------------------------")
        print(self.name, " | ", self.price, " | ", self.rating)
        print("------------------------------------")
        print()

    # def showFoodItem(self):
    #     print("************************************")
    #     print(self.name, " | ", self.price, " | ", self.rating)
    #     print("************************************")
    #     print()


item1 = FoodItem("Poori Channa", 105, 4.5)
item2 = FoodItem("Dal Kachori", 87, 4.8)
item3 = FoodItem("Samosa", 18, 4.0)

item1.showFoodItem()
item2.showFoodItem()
item3.showFoodItem()
