johnsAge = 20
jenniesAge = johnsAge

# johnsAge and jenniesAge are reference variables which
# points to the same container

print("johnsAge is:", johnsAge, "HashCode is:", hex(id(johnsAge)))
print("jenniesAge is:", jenniesAge, "HashCode is:", hex(id(jenniesAge)))

# Update Operation
# johnsAge = 22
#
# print("johnsAge is:", johnsAge, "HashCode is:", hex(id(johnsAge)))
# print("jenniesAge is:", johnsAge, "HashCode is:", hex(id(jenniesAge)))

# Delete Operation
del johnsAge

print("jenniesAge is:", jenniesAge, "HashCode is:", hex(id(jenniesAge)))
