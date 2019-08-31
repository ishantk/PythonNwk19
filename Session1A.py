# Model : Storage Container
# 1. Single Value Container
# 2. Multi Value Container
#    Homogeneous
#    Hetrogeneous

# Single Value Containers

# Container Creational Statements
# in ram area and are temporary
# LHS is name of storage container and RHS is the data in storage container
name = "cisco"
ipAddress = "192.168.20.1"
time = 2

# Update Statements
# We can update data in Storage containers
ipAddress = "192.168.20.4"

# Read Statements to read data from containers
print("name is:", name)
print("IP Address is:", ipAddress)
print("Time is:", time, "hours")

# Delete Container
del ipAddress
# print("IP Address is:", ipAddress) err


