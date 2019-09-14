# List is MUTABLE : we can update, delete or add data in the list
names = ["John", "Jennie", "Jim"]
names[0] = "Fionna Flynn"  # Update Operation, 0th index previous value is modified
names.append("Kim")  # append is a function of list, which will add the data in the end :)

print(names)

# Tuple is IMMUTABLE : we cannot update
newNames = ("John", "Jennie", "Jim")
# newNames[0] = "John Watson" #err
# del newNames[0]             #err
# newNames.append("Kim")      #err
print(newNames)

# PS: If we create a Tuple we cannot perform operations like update, delete or add
#     Its a kind of a constant for us
#     We can perform loops, indexing, slicing, other operations

