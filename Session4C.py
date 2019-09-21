S1 = {1, 2, 3, 'a', 'b'}
S2 = {1, 'a', 'b'}

print(1 in S1)

print(S2.issubset(S1))
print(S1.issuperset(S2))

# Built in function union rather than | operator
S3 = S1.union(S2)    # but what happens when we do Union Operation
print("S1 now is:", S1)
print("S2 now is:", S2)
print("S3 is:", S3)

# S1.difference(S2)
# S1.intersection(S2)
# S1.symmetric_difference(S2) # Explore them :)

# PS: No Indexing is happening in SETS
# print(S1[0]) error
# Set Supports Hashing and we cannot get a single element from Set
# We need to use enhanced for Loop to read the elements in set

for elm in S1:
    print(elm, end=" ")