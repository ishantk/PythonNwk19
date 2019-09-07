# Logical Operators
# and, or

# and yields true result if both conditions are true
# or yields true if any one is true

physics = 95
chemistry = 90
maths = 90

print(">> Can Student be a CS Engineer?", maths >= chemistry and maths >= physics)
print(">> Can Student be a CS Engineer?", maths >= chemistry or maths >= physics)
print(">> Can Student be a CS Engineer?", not(maths >= chemistry or maths >= physics))
