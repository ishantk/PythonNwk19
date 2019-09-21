# Built-Ins on Strings

name = "John Watson"
name.upper()    # . is to execute some built in function of String
                # upper will change the String to upper case

print(name)
# Strings are IMMUTABLE. They Cannot be Changed !!
# If we perform any manipulation i.e. modification on String it will not come up
# Rather, a new String will be generated

newName = name.upper()
print(newName)

quote = "work hard and get luckier"
myQuote = quote.capitalize()

print("quote:", quote)
print("myQuote", myQuote)

#        0123.......
names = "John, Jennie, Jim, Jack, John, Joe"
idx = names.index("h")
print("idx is:", idx)

# we are extracting index
idx = names.index("Jennie")  # From where Jennie's J will begin
print("idx is:", idx)

newNames = names.replace('J', 'K')
print(">> names:", names)
print(">> newNames:", newNames)

# Extracting a sub string from a string | Slicing
myName = names[6:12]
print(myName)

# num = names.count("John", 0, len(names))
num = names.count("J", 0, len(names))
print(">> J Occurred {} times".format(num))


quote = "work hard and get luckier"
words = quote.split(" ")
print(words)

individualNames = names.split(",")
print(individualNames)

# String Concatenation
salutation = "Mr."
fname = "George"
lname = "Watson"

fullName = salutation + " " + fname + " " + lname   # Concatenation
print(fullName)

email = "john@example.com"

if email.endswith(".com"):
    print(">> Email ends with .com")
else:
    print(">> Email does not ends with .com")

fileName = "Hello.mp3"
if fileName.endswith(".mp3"): # startsWith
    print(">> An Audio File")
else:
    print(">> Not An Audio File")

# number = 20     # int
number = "20"     # String

if number.isdigit():
    print(">> Its a Digit")
else:
    print(">> Its not a Digit")

# We have so many other is functions which we can use on Strings
# Explore all these built in functions : Refer python documentation
# https://docs.python.org/3/tutorial/introduction.html#strings

