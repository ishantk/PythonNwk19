# Default Values for our inputs
# RULS : default value to an input can be given if right input has a default value
def addNumbers(num1=1, num2=12, num3=5):
    sum = num1 + num2 + num3
    print(">> Sum is:", sum)

addNumbers(10, 20, 30)
addNumbers(num1=11, num3=22, num2=17)  #Keyword Arguments
addNumbers(10, 20)
addNumbers()

print(">> HashCode of addNumbers is:", addNumbers)

# Update Operation on Function
# Re-Defining the same Function
def addNumbers(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    print(">> Sum is:", sum)

print(">> HashCode of addNumbers now after re-defining is:", addNumbers)

# addNumbers(1, 2, 3)
addNumbers(10, 20, 30, 40)