"""

    Sequences in Python
        List
        Tuple
        String
        Set
        Dictionary

    Operations on Sequences:
        1. Concatenation
        2. Repetition
        3. Membership Testing
        4. Slicing
        5. Indexing

"""

# List
students = ["John", "Jennie", "Jim", "Jack", "Joe"]
ages = [20, 22, 23, 33, 37]
registrationNumbers = [101, 102, 103, 103, 104]
print(students)
print(type(students))

# Operations on List

# 1. Concatenation
# PS: Concatenation Operation on 2 Lists will generate a new List
newStudents = students + ["Fionna", "Mike", "Lee"]
print(students + ["Fionna", "Mike", "Lee"])
print(students)         # No Change in Students
print(newStudents)      # new list with Changes

concatenatedList = students + ages + registrationNumbers
print("concatenatedList is:", concatenatedList)

print() # to have an empty line

# 2. Repetition
print(students * 2)
print(students * 3)
print(students)

print()

# 3. Membership Testing
print("John" in students)
print(1001 in concatenatedList)
print(1001 not in concatenatedList)

# 4. Indexing
# Data in the List is indexed from 0 to n-1 where n is size of list
print(students[0])
print(students[3])

# 5. Slicing
# Where we wish to extract multiple elements form list
print(students[1:4])    # From index 1 till index 3, 4 not inclusive

print(concatenatedList[5:9])

