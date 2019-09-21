routers = {"router1": "198.160.0.1", "router2": "198.160.0.2",
           "router3": "198.160.0.3", "router4": "198.160.0.4"}

# Dictionary is collection of key value pairs
# Just Like Word Meaning

print(routers)
print(type(routers))

# Instead of Indexing, we have keys which we only give
# Keys are Unique: If you use the same key again, data will be updated
print(routers["router2"]) # get the Value here

# Update Operations
routers["router1"] = "198.170.1.1"
print(routers)

# Delete Operation
del routers["router2"]
print(routers)

# routers.clear()
# print(routers)

# print(routers.keys(), type(routers.keys()))
# get the keys from Dictionary as a list :)
keys = list(routers.keys())
values = list(routers.values())

print(keys)
print(values)

# Use a Loop to iterate in Dictionary

for key in keys:
    print(key, routers[key])

# Add a new Key with value in Dictionary :)
routers["router5"] = "198.0.0.1"

print(routers.items())
items = list(routers.items())
print(items)

print(items[0])
print(items[1])
print(items[2])

# Application : Zomato
dishesRestaurantA = {"Noodles":200, "Sandwich":100, "Pizza":350}
dishesRestaurantB = {"Noodles":150, "Sandwich":200, "Pizza":750, "VegSoup":120}

# List of Dictionaries :)
restaurants = [dishesRestaurantA, dishesRestaurantB]

# List of Lists, Set of Sets, Dictionary of Dictionaries
# List of Sets, Set of Lists, List of Dictionaries.....


# PS: When we will use Web Services we have some response which ic Dictionary and further dictionary may contains dictionaires or lists
#     JSON : Java Script Object Notation

