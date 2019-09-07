# Bitwise Operators

a = 8       # 1 0 0 0
b = 12      # 1 1 0 0

c = a & b   # 1 0 0 0 | 8
d = a | b   # 1 1 0 0 | 12
e = a ^ b   # 0 1 0 0 | 4

print(">> c is:", c)
print(">> d is:", d)
print(">> e is:", e)

# Shift Operators
# >> <<

x = 8
y = x >> 2  # Divide by 2 power 2 | Base is always 2
z = x << 3  # Multiple by 2 power 3 | Base is always 2

print("y is:", y)
print("z is:", z)


