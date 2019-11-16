import os

print(os.getcwd())
print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid())  # Parent Process is PyCharm for our Python Program

pathToDir = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/routers-nov.csv"
print("If Downloads Directory available:", os.path.exists(pathToDir))
print("If routers-nov.csv file available:", os.path.exists(pathToFile))


# path = "/Users/ishantkumar/Downloads/Python-Nov"
# print("If Python-Nov Directory available:", os.path.exists(path))
# os.mkdir(path)
# os.rmdir(path) # This remove is unsafe as in contents will not go in your trash or recycler bin

# print(os.getcwd())
# os.chdir("/Users/ishantkumar/Downloads/Python-Nov")
# print(os.getcwd())

files = os.walk("/Users/ishantkumar/Downloads/Python-Nov")
print(">> files: ", files)

allFiles = list(files)

for file in allFiles:
    print(">> ",file)