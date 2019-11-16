file = open("Session3.py", "r")

print(file.tell()) # Get to know the position of cursor

# We are just reading 15 characters i.e. bytes of file
data = file.read(15)
print(">>data is:", data)

data = file.read(30)
print(">> data is:", data)

file.seek(100)
data = file.read(30)
print(">> data is:", data)

print(file.tell())

file.close()  # Release Memory Resources

# tell -> tell the location of cursor in your file which is by default 0 when we open a file
# seek -> take the cursor to some corresponding location as required by you
