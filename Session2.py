# Operators
# They help to perform a computation on data storage containers

# input/int is a function
# function takes something as input and gives back result

dataSize = int(input("Enter Size of Data: "))
bandWidth = int(input("Enter BandWidth: "))

#   / -> Operator

# transmissionDelay = dataSize / bandWidth
transmissionDelay = dataSize // bandWidth

print("Transmission Delay is:", transmissionDelay)
print(type(transmissionDelay))

# Arithmetic Operators : +, -, *, **, /, //, % (Modulus)

a = 10
b = 3
c = a % b
print(c)  # Remainder : 1 :)

num = 2 ** 3        # 2 power 3
print(">> num is:",num)
