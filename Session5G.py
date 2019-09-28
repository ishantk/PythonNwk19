# Passing Single Value
def squareOfNumber(number):
    print("** number is:", number, "and HashCode is:", hex(id(number)))
    number = number * number
    print("** number now is:", number, "and HashCode is:", hex(id(number)))


num = 11
print(">> num is:", num, "and HashCode is:", hex(id(num)))

squareOfNumber(num)

print(">> num now is:", num, "and HashCode is:", hex(id(num)))

