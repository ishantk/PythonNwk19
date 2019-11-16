file = open("Session3.py", "r")
# file = open("/Users/ishantkumar/Downloads/TaskPage.txt", "r")

print(type(file)) # TextIOWrapper | IO is Input Output

# Read All the Contents of File
fileContents = file.read()
print(fileContents)

print("====Re-Reading====")

# Re-Reading the Same File Again
fileContents = file.read()
print(fileContents)

# Once we have read a file, we wont be able to re-read it !!

# Close the File and it wont be further available to read
file.close()

# print("====Re-Reading after closing the file====")

# Re-Reading the Same File Again
# fileContents = file.read()
# print(fileContents)


print(file.closed)

if(file.closed):
    print(">> We Cannot Read")
else:
    print(">> Lets Read")
