file = open("Session3.py", "r")


# fileContents = file.read()

"""
line = file.readline()
print(">> line is:", line)

line = file.readline()
print(">> line is:", line)

line = file.readline()
print(">> line is:", line)

line = file.readline()
print(">> line is:", line)

# readline function will read the file line by line and shall always give the next line

"""

# Read All the lines of a file as a list of strings
lines = file.readlines()

print(lines)
print(type(lines))

count = 0

for line in lines:
    print(line)

    if line.startswith("print"):
        count = count + 1
        print("****",line[6:9],"****")


print(">> {} lines starts with print".format(count))

