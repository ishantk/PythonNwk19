# List of Lists
cart = [
            #  0        1        2
            ["Shoe", "Mobile", "TV"],   # 0
            [800, 30000, 50000]         # 1
       ]

print(len(cart))    # 2
print(cart[0])      # ["Shoe", "Mobile", "TV"]

print(len(cart[0])) # 3
print(cart[0][1])   # Mobile

print("=========")
for i in range(0, len(cart)):   # i will have values: 0 and 1
    for j in range(0, len(cart[i])): # len(cart[0/1]) : 3 | j will have values 0, 1 and 2
        print(cart[i][j])  # 00, 01, 02 | 10, 11, 12

print("=========")

print()
print("=========")
for i in range(0, len(cart[0])):
    print(cart[0][i], "\t\t", cart[1][i])

print("=========")

print()

numbers = [11, 56, 23, 12, 98]
idx = numbers.index(23)
print(idx)

# Explore more Built in Functions on list
# write list name and . operator to get hints for functions in list :)

