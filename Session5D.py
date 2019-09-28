# VARIABLE ARGUMENTS IN FUNCTION
# *args -> Variable Arguments and type becomes tuple
def addNumbers(*args): # *anyName
    print(args)
    print(type(args))

    sum = 0

    for elm in args:
        sum = sum + elm

    print(">> Sum is:", sum)


addNumbers(10, 20)
addNumbers(10, 20, 30, 40, 50)
