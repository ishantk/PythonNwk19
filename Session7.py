"""

    OOPS Principle:

    1. Think of an Object
       Restaurant : name, phone, address, rating, pricePerPerson

    2. Create its Class

    3. From Class Create a real Object in Memory

"""

class Restaurant:
    # Constructor
    # So that we can have some standard attributes with values in objects
    # self is ref variable which will hold HashCode of current object
    # __init__ is executed the moment object is created in memory
    def __init__(self, name, phone, address, rating, pricePerPerson):
        self.restaurantName = name
        self.phone = phone
        self.address = address
        self.rating = rating
        self.pricePerPerson = pricePerPerson

    def showRestaurantDetails(self):
        print("===", self.restaurantName, "====")
        print(">>", self.address, " | ", self.phone, " | ", self.rating)


# r1 is a Reference Variable which will hold HashCode of Restaurant Object
r1 = Restaurant("John's Cafe", "+91 99999 88888", "Redwood Shores", 4.5, 200)
r2 = Restaurant("Picnic Square", "+91 98765 88888", "Country Homes", 5, 500)
print(">> r1 is:", r1)
print(">> Dictionary of r1 is:", r1.__dict__)

print()

print(">> r2 is:", r2)
print(">> Dictionary of r2 is:", r2.__dict__)

r1.showRestaurantDetails()
r2.showRestaurantDetails()