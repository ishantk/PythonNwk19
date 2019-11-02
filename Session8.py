# Amazon e-Commerce Platform
# MobilePhone | Shoe

"""
    OOPS Principle
    1. Think of an Object
    2. Associate data and create its class
    3. From Class create Real objects in memory

    MobilePhone
        pid, name, brand, price, os, ram, memory

    Shoe
        pid, name, brand, price, size, color


"""

"""
class MobilePhone:

    def __init__(self, pid, name, brand, price, os, ram, memory):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.os = os
        self.ram = ram
        self.memory = memory


    def showMobilePhone(self):
        print("==",self.pid,"|",self.name,"==")
        print(self.brand)
        print(self.price)
        print(self.os)
        print(self.ram)
        print(self.memory)

class Shoe:

    def __init__(self, pid, name, brand, price, size, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.size = size
        self.color = color


    def showShoe(self):
        print("==",self.pid,"|",self.name,"==")
        print(self.brand)
        print(self.price)
        print(self.size)
        print(self.color)


m1 = MobilePhone(101, "iPhoneX", "Apple", 70000, "iOS", 4, 256)
m1.showMobilePhone()
print(m1.__dict__)

s1 = Shoe(201, "AlphaBounce", "Adidas", 8000, 9, "Black")
s1.showShoe()
print(s1.__dict__)

"""

# WHY INHERITANCE
# Inheritance : All About reducing the effort of writing repetitive code again and again
# RE-USABILITY

class Product:  #Parent

    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProduct(self):
        print("==", self.pid, "|", self.name, "==")
        print(self.brand)
        print(self.price)

class MobilePhone(Product): # Child # IS-A Relationship -> MobilePhone IS-A Product

    def __init__(self, pid, name, brand, price, os, ram, memory):
        Product.__init__(self, pid, name, brand, price)
        self.os = os
        self.ram = ram
        self.memory = memory

    def showMobilePhone(self):
        Product.showProduct(self)
        print(self.os)
        print(self.ram)
        print(self.memory)

class Shoe(Product):

    def __init__(self, pid, name, brand, price, size, color):
        Product.__init__(self, pid, name, brand, price)
        self.size = size
        self.color = color

    def showShoe(self):
        Product.showProduct(self)
        print(self.size)
        print(self.color)


m1 = MobilePhone(101, "iPhoneX", "Apple", 70000, "iOS", 4, 256)
s1 = Shoe(201, "AlphaBounce", "Adidas", 8000, 9, "Black")

# p1 = Product()

m1.showMobilePhone()
s1.showShoe()


print(m1.__dict__)
print(s1.__dict__)