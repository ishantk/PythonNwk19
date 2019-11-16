file1 = open("Session3.py", "r")


# We are just reading 100 characters i.e. bytes of file
data = file1.read(100)
print(">>data is:", data)

file1.close()

file2 = open("/Users/ishantkumar/Downloads/copy-nov.txt", "w")    # write mode
file2.write(data)

file2.close()

print(">> File Contents Copied !!")