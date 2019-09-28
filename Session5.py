"""

    Maths:
    f(x) = x*x + 1
        > f is name of function
        > x is input
        > x*x + 1 is definition

    f(1) = 1*1 + 1 => 2
    f(2) = 2*2 + 1 => 5

    wholeSquare(x, y) = x*x + y*y + 2*x*y
        > wholeSquare is name of function
        > x and y are inputs
        > x*x + y*y + 2*x*y is definition

    Python Programming:
        Function
            1. name
            2. Inputs(may or may not be) | Arguments or Parameters
            3. Definition -> What function will do for us
                             Set of some python instructions which will be executed in a sequence

            4. acknowledgement (may or may not be)
                eg: we will return back the result

            example: in real world

                carService (wheelBalancing:no)
                    1. Open Engine and Oil it
                    2. Clean Filters
                    3. Balance Wheels
                    4. Check AC
                    5. Wash Vehicle

                    return: call me on my phone

                prepareTea(milk:1, sugar:1, cups:5)
                    1. Take Vessel
                    2. Pour Water
                    3. Boil Water
                    4. Add Tea Leaves
                    5. Put in a cup

                    return: serve when done


"""
# 1. Why Functions are needed ?
"""
num1 = 10
num2 = 20
sum = num1 + num2
print(">> sum of {} and {} is {}".format(num1, num2, sum) )


num1 = 11
num2 = 65
sum = num1 + num2
print(">> sum of {} and {} is {}".format(num1, num2, sum) )

# We may need to add 2 numbers several times !!


amount = 500
taxes = 0.18
taxesOnAmount = amount * taxes
print(">> taxesOnAmount:", taxesOnAmount)

amount = 750
taxesOnAmount = amount * taxes
print(">> taxesOnAmount:", taxesOnAmount)

# We may need to find taxes on several amounts again and again

# >> Certain Statements are suppose to be executed several times and we cannot decide them by loops
"""


# We need Functions in which we will write these instructions
#  and will execute the function whenever needed
def addNumbers(num1, num2):
    sum = num1 + num2
    print(">> sum of {} and {} is {}".format(num1, num2, sum))

def calculateTaxes(amount):
    taxes = 0.18
    taxesOnAmount = amount * taxes
    print(">> taxesOnAmount:", taxesOnAmount)

def printAppName():
    print("**********************")
    print(">> WhatsApp <<")
    print(">> Stay Connected <<")
    print("**********************")

# Execute Functions
addNumbers(10, 20)
addNumbers(11, 75)

calculateTaxes(500)
calculateTaxes(750)
calculateTaxes(1250)

printAppName()

