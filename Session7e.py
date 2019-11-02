# Class Vs Object
# Whatever is in the Class  -> Belongs to Class
# In the class whatever is with self -> Belongs to Object

class FoodItem:

    total = 0  # Property of Class

    def __init__(self, name, price, count):
        self.name = name                        # self -> property of Object
        self.price = price
        self.count = count
        FoodItem.total = FoodItem.total + 1     # FoodItem -> property of Class

    def incrementQuantity(self):
        self.count = self.count + 1

    def decrementQuantity(self):
        self.count = self.count - 1

    def showFoodItem(self):
        print(">> For {} Please Pay {} for Quantity {}".format(self.name, self.price*self.count, self.count))


item1 = FoodItem("Poori Channa", 110, 2)     # __init__ will be executed
item2 = FoodItem("Samosa", 20, 1)            # __init__ will be executed

item3 = item2

item1.incrementQuantity()   #3
item1.incrementQuantity()   #4
item1.decrementQuantity()   #3

item2.incrementQuantity()
item2.incrementQuantity()
item3.decrementQuantity()

item1.showFoodItem()
item3.showFoodItem()

# FoodItem.showFoodItem(item1)

print(">> item1 is:", item1)
print(">> item2 is:", item2)
print(">> item3 is:", item3)

print(">> You have Ordered a total of {} separate items".format(FoodItem.total))

# 2 Different FoodItems are thr ?
# How we show User the different FoodItems which he is buying ?
