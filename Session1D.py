# Read data from User as input
# ipAddress = "192.168.20.1"  # HardCode

# Dynamic Way of creating Storage Containers i.e. Data to be taken as input from User
ipAddress = input("Enter an IP address: ")
print(">> IPAddress is:", ipAddress)
print(">> type of IPAddress", type(ipAddress))

hours = input("Enter Hours: ")
print(">> Hours is:", hours)
print(">> type of Hours is:", type(hours))

# PS: with input function whatever we are reading is always text i.e. string
#     with print function whatever we will print will always be text i.e. string

# We have option to convert textual data i.e. str in any other type as required by us
age = int(input("Enter Age: "))
print(">> age is:", age)
print(">> type of age is:", type(age))
