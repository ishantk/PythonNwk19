quotes = """
Search the Candle, rather than cursing the darkness
Work Hard, Get Luckier
"""

print(quotes)
print(type(quotes))

file = open("/Users/ishantkumar/Downloads/quotes-nov.txt", "w")
# open function will give an error if file is not available while read operation
# but open function will create a file if not available while write operation

# file.write(quotes)
# file.close()    # We are releasing memory resources

# print(">> File Created and Data Written")

print(file.tell())
# Find the logic how will you seek at the end of file
# file.seek(?) # what we should write in seek to move the cursor to end of file
# print(file.tell()) -> Here you will get the size of file !!
