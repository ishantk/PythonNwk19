# Lets Explore more of List and some of its functions
technologies = ["AI", "Android", "Hadoop", "JEE", "Node", "Angular"]

print(technologies)

# Update Data in List
technologies[1] = "Flutter"

print(technologies)

del technologies[2]

print(technologies)
print(technologies[2])  # positive indexing
print(technologies[-2]) # negative indexing (start from -1 from the end)

print(technologies[0:2])
# Exploration : slicing with -ves :)

rollNumbers = [1, 2, 3, 4, 5, 4]
rollNumbers.pop(2)  # Pop will remove element on the basis of index
print(rollNumbers)


rollNumbers.remove(4)   # remove removes the 1st matching element
print(rollNumbers)


# built in function of list : pop and remove
# to access functions of list we need to use . operator
# functions or methods or routine or procedures :)
