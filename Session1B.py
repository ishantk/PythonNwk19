ipAddress = "192.168.20.1"
johnsCoffeeShop = "Cafe Delight"
hours = 2

# Copy Operation | Reference Copy i.e. HashCode is getting copies
myRouterIPAddress = ipAddress

# Check type of data storage container
print(ipAddress, "type is:", type(ipAddress))
print(johnsCoffeeShop, "type is:", type(johnsCoffeeShop))
print(hours, "type is:", type(hours))

# Check HashCode where data is stored
print("ID of IP Address is:", id(ipAddress))
print("ID of myRouterIPAddress is:", id(myRouterIPAddress))


print("ID of IP Address is:", hex(id(ipAddress)))
print("ID of myRouterIPAddress is:", hex(id(myRouterIPAddress)))
print("ID of IP Address is:", oct(id(ipAddress)))
print("ID of IP Address is:", bin(id(ipAddress)))

# print, type, id, hex, oct and bin are known as functions
# function
# f(x) = x+1
# f(1) = 2
# f(2) = 3


# PS: ipAddress, johnsCoffeeShop, hours, myRouterIPAddress are called Reference Variables
#     They hold HashCode of data
#     HashCode is a unique number associated to every storage container in the memory
#     HashCode may be represented by us in decimal(id), hex, oct or bin


