# Dictionary as Storage Container
employee = {"eid" : 101, "name" : "John", "salary" : 50000}
print(employee)
print(type(employee))

print()

"""
    JSON : Java Script Object Notation
           Its just like dictionary i.e. key value pair but is always string
           Its always gonna start as dictionary and may have list in it as well
"""

import json

# We are converting a Python Dictionary into JSON String | dumps
# JSON will be textual or String representation of Python Dictionary
jsonEmployee = json.dumps(employee)
print(jsonEmployee)
print(type(jsonEmployee))
# jsonEmployee is a JSON String

print()

# JSON to Python Dictionary | loads
pyEmployee = json.loads(jsonEmployee)
print(pyEmployee)
print(type(pyEmployee))



