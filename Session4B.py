A = [1, 2, 3, 4, 5, 2, 3]   # Duplicate Data
X = {1, 2, 3, 4, 5, 2, 3}   # No Duplicate Data (Elements may be unordered duse to a technique called Hashing)

print(A, type(A))
print(X, type(X))

# Convert List into Set
# Reason? So that we can have unique elements i.e. remove duplicates
B = set(A)
print(B, type(B))

# Data in Sets
P = {1, 2, 3, 4}
Q = {3, 4, 5, 6}

R = P | Q # Union Operation on Sets
print(R)  # Merge Data in both sets

S = P & Q # Intersection Operation on Sets
print(S)  # Common Elements

T = P - Q # Difference Operation on Sets
U = Q - P
print(T) # 1 2
print(U) # 5 6

# We are here not using any built in technique
elements = []

for elm in T:
    elements.append(elm)

for elm in U:
    elements.append(elm)

print(elements)
