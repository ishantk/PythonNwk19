# OOPS in Python
# Object Oriented Programming Structure
# > Object
# > Class

# Core Fundamental in above topic is Object
# Everything revolves around Object !!
"""
    1. Real Life
    Object : Anything around you which you can see, touch
             exists in Reality
             eg: Chair, Table, Laptop, Glasses, Bottle, Fan

    Class : Representation how an Object will Look Like !!
            Drawing of an Object

    OOPS Principle :
    1. THINK OF AN OBJECT
    2. CREATE ITS DRAWING
    3. FROM DRAWING CREATE OBJECT

    eg: We wish to construct a Home !!
        You may visit an Architect !!

        Architect shall listen to our requirements
        Architect shall start thinking and visualising the Home
        Architect shall create drawings
        Handover drawings to client to get the real home constructed


     2. Computer Science
     Object : A Multi Value Container
              Can hold lot of data as key value pairs just like dictionary
              Can be homogeneous or Hetrogeneous

     Class : Textual Representation of an Object
             Write the Code which represents Object

    OOPS Principle :
    1. THINK OF AN OBJECT
    2. CREATE ITS DRAWING
    3. FROM DRAWING CREATE OBJECT


    1. THINK OF AN OBJECT
       You study Requirements for Problem Statement
       You will find certain terms which will have lot of data associated with it

       example     : Food Delivery App [Zomato]
       requirements: List Restaurants and Let Users order from the menu

       Focus on Term which has lot of Data Associated with it !!

       User     | Object
        name    | Attributes
        phone
        email
        age
        gender
        address
        .
        ...

       Restaurant | Object
        name      | Attributes
        phone
        email
        address
        type
        operatingHours
        ratings
        landMarks

       Order    | Object
        oid     | Attributes
        date
        time
        quantity
        foodItems[]
        amount
        taxes
        discounts

       Menu
       .
       ..
       ....


        Zomato Use Case:

        // 1. Think Of Object
        Object
        -------
        Restaurant

        Attributes
        ----------
        name
        phone
        email
        address
        type
        operatingHours
        ratings
        landMarks

"""

# We already have single value containers
# We do have tuple, list, set, dictionary etc...

# restaurant = {"name":"Pandit Paranthe", "phone":"+91 99999 88888"}

# Customizations : We would may require lot of things which dictionary will not support

# 2. Create Its Drawing
#    A User Defined Type
class Restaurant:
    pass

# 3. Create Real Object from Drawing i.e. Class

# Object Construction Statement
r1 = Restaurant()
r2 = Restaurant()
# r1 and r2 are Reference Variables Which will hold HashCode of Objects constructed in memory
print("r1 is:", r1)                      # HashCode
print("type of r1 is:", type(r1))        # Data Type
print("Object Contains:", r1.__dict__)   # Prints Attributes along with values as dictionary in an Object

print("--------")

print("r2 is:", r2)                      # HashCode
print("type of r2 is:", type(r2))        # Data Type
print("Object Contains:", r2.__dict__)   # Prints Attributes along with values as dictionary in an Object

# Reference Copy Operation
r3 = r1

print("--------")

print("r3 is:", r3)                      # HashCode
print("type of r3 is:", type(r3))        # Data Type
print("Object Contains:", r3.__dict__)   # Prints Attributes along with values as dictionary in an Object

# Till now Constructed Objects are Empty
# Operations on Object
# 1. Write Data in Object
r1.name = "Changs Chinese"
r1.address = "Redwood Shores"
r1.type = "Chinese"
r1.pricePerPerson = 200
r3.landMark = "Brown Tower"
r3.rating = 3.5

r2.name = "Chawlas"
r2.address = "Country Homes"
r2.rating = 4.0

print("*****AFTER ADDING ATTRIBUTES******")
print(">> r1 dictionary:", r1.__dict__)
print(">> r2 dictionary:", r2.__dict__)
print(">> r3 dictionary:", r3.__dict__)

# 2. Update Data in Object
r3.address = "Pristine Magnum"
r1.rating = 4.2

r2.pricePerPerson = 500

# RULE OF Object Attributes: If we have an attribute, value is updated else a new attribute shall be created

print("*****AFTER UPDATING ATTRIBUTES******")
print(">> r1 dictionary:", r1.__dict__)
print(">> r2 dictionary:", r2.__dict__)
print(">> r3 dictionary:", r3.__dict__)

# 3. Delete Attributes of Object or Delete Object ItSelf
# del r1.type
# del r2.address

print("*****AFTER DELETING ATTRIBUTES******")
print(">> r1 dictionary:", r1.__dict__)
print(">> r2 dictionary:", r2.__dict__)
print(">> r3 dictionary:", r3.__dict__)

# del r2
# print(">> r2 dictionary:", r2.__dict__) # Error as r2 is now not in memory

# del r1
# print(">> r3 dictionary:", r3.__dict__)

print()

# 4. Read Selected Attributes
print("*****Read Selected Attributes******")
print(r1.name, "is located at", r1.address)
print(r2.name, "is located at", r2.address)




