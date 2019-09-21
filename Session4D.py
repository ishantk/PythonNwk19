S = {1, 2, 3, 4, 'A', 'B'}

# We can add data in Set
S.add('C')
S.add(2)
print(S)

# Remove Data from Set
S.remove(2)
S.remove('A')

print(">> S now is:", S)

S.clear() # Removes all and also works with list

print(">> S after clear is:", S)


S1 = {1, 2, 3, 'a', 'b'}
S2 = {1, 'a', 'b'}

# Set
# add will not add up the Sets and it adds only the data :)
# S3 = {"A", "B"}
# S3.add(S1)
# print(">> S3 is:", S3)

L1 = list(S1)
print(">> L1 is:", L1)
