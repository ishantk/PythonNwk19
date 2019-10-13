# Let us Optimize how we code Objects

# 1. Think of an Object
#     Cab : title, price, numOfRiders

"""
# 2. Create Class i.e. Drawing
class Cab:
    pass

# 3. Create Objects in memory from Class
c1 = Cab()
c2 = Cab()
c3 = Cab()

# Challenge
# 1. Code Repetition for Creating Attributes
# 2. We may make a mistake in spellings
c1.title = "UberGo"
c1.prce = 49
c1.numOfRiders = 4

c2.title = "Moto"
c2.price = 20
c2.numOfRides = 1

c3.title = "Moto"
c3.price = 20
c3.numberOfRiders = 1
"""

# Lets write Optimized Class Code
class Cab:

    # Function: Pre-Defined: We will create it
    #           Property of class
    # __init__ is helping us to create a standard code where each object will have same attributes with same values
    # DEFAULT CONSTRUCTOR
    # def __init__(self):
    #     print(">> init executed")
    #     print(">> self is:", self, "and type is:", type(self))
    #     print("-----------------")
    #
    #     self.title = "NA"
    #     self.price = 0
    #     self.numOfRiders = 0


    # if we define constructor again, previous constructor will be removed
    # Now, we have a Constructor with inputs | PARAMETERIZED OR ARG CONSTRUCTORS
    def __init__(self, title, price, numOfRiders):
        self.title = title
        self.price = price
        self.numOfRiders = numOfRiders

    # Function: Property of class
    def showCab(self):
        print("===============")
        print("Cab:", self.title)
        print("Price: \u20b9", self.price)
        print("Riders:", self.numOfRiders)
        print("===============")
        print()


# c1 = Cab()  # The moment we create object, init is executed | Constructor
# c2 = Cab()
# c3 = Cab()

c1 = Cab("UberGo", 49, 4)   # The moment we create object, init is executed | Constructor
c2 = Cab("Moto", 20, 1)
c3 = Cab("Premier", 100, 4)

print(">> c1 is:", c1, " and type is:", type(c1))
print(">> c2 is:", c2, " and type is:", type(c2))
print(">> c3 is:", c3, " and type is:", type(c3))

# self in __init__ is a Reference Variable which holds the HashCode of Object

# c1.title = "UberGo"
# c1.dropOff = "20 mins"
#
# c2.title = "Moto"
# c3.title = "Premier"

# c1.driver = "John"
# c1.regNum = "DL10AB1234"
#
# del c1.title

print(">> c1 dictionary is:", c1.__dict__)
print(">> c2 dictionary is:", c2.__dict__)
print(">> c3 dictionary is:", c3.__dict__)

"""
print("===============")
print("Cab:",c1.title)
print("Price: \u20b9", c1.price)
print("Riders:", c1.numOfRiders)
print("===============")
print()

print("===============")
print("Cab:",c2.title)
print("Price: \u20b9", c2.price)
print("Riders:", c2.numOfRiders)
print("===============")
print()

print("===============")
print("Cab:",c3.title)
print("Price: \u20b9", c3.price)
print("Riders:", c3.numOfRiders)
print("===============")
print()
"""

# c1.showCab() # -> Gets translated like this -> Cab.showCab(c1)
# c2.showCab()
# c3.showCab()

Cab.showCab(c1)
Cab.showCab(c2)
Cab.showCab(c3)





