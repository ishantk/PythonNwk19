# We have created 4 single value containers
router1 = "192.168.20.1"
router2 = "192.168.20.2"
router3 = "192.168.20.3"
router4 = "192.168.20.4"

# we can create a multi value container
# 1. Multi Value Container : Tuple
# routers = "192.168.20.1", "192.168.20.2", "192.168.20.3", "192.168.20.4"      # Syntax1
myRouters = ('192.168.20.1', "192.168.20.2", """192.168.20.3""", "192.168.20.4", "192.168.20.4")  # Syntax2
print(myRouters)
print(">> type of routers", type(myRouters))

print("--------------")

# 2. Multi Value Container : Set : Give Unordered Output. but Why ? To make data unique
routers = {"192.168.20.1", "192.168.20.2", "192.168.20.3", "192.168.20.4", "192.168.20.4"}
print(routers)
print(">> type of routers", type(routers))

print("--------------")

# 3. Multi Value Container : List
routers = ["192.168.20.1", "192.168.20.2", "192.168.20.3", "192.168.20.4", "192.168.20.4"]
print(routers)
print(">> type of routers", type(routers))

print("--------------")

# 4. Multi Value Container : Dictionary
#    Data becomes more meaningful
routers = {"router1":"192.168.20.1", "router2": "192.168.20.2", "router3":"192.168.20.3"}
print(routers)
print(">> type of routers", type(routers))


# Info
# User : name phone age gender address


# List and Tuple we can get the data based on indexing technique :)
# 0 to n-1
print(myRouters[1])
