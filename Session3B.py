data = [10, 20, 30, 40, 50]

# refer -> ASCII Table http://www.asciitable.com/
names = ["Anna", "John", "Fionna", "anna", "Mike", "Kim"]
# length = len(data)
# print("Length of data is:", length)
print("Length of data is:", len(data))
print("Max of data is:", max(data))
print("Min of data is:", min(data))

print()

print("Max of names is:", max(names))
print("Min of names is:", min(names))

print()

# Put up a Loop on List
# i : 0, 1, 2, 3, 4, 5
# for i in range(0, len(names)): # 0 inclusive and len(names) i.e. 6 not inclusive and less than 6 i.e. till 5
#     print(names[i])

for i in range(0, len(names), 2):  # Step of 2
    print(names[i])


print()

# Read All Elements in List in sequence
# Enhanced For Loop

for name in names: # Automatically values will be copied into name from names 1 by 1
    print(name)

# List Comprehension in Python : Explore more different types of List Comprehensions
print([x**2 for x in data])

print()

# numbers = list(range(1, 101, 2))
numbers = list(range(0, 101, 2))
print(numbers)