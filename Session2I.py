# Iterations or Loops in Python
# while and for

documentName = "MyResume.pdf"
copy = 1

# Whatever we have written in while block it will be executed till time condition matches
# till time condition gives True as result
while copy <= 10:
    print(">> Printing", documentName, "on Printer Copy#", copy)
    # copy += 1
    copy += 2

# Below Statement is out of the While Block

print("==Thank You==")
documentName = "LearningPython.pdf"

# for i in range(1, 11):
for i in range(1, 11, 2):
    print(">> Printing", documentName, "on Printer Copy#", i)

