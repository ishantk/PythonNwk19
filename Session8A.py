# What is Inheritance

# Rule of Inheritance
# If Child has no function or attribute, it can access from Parent

class Employee:

    # Constructor and showEmployee belongs to Class Employee
    # But Attributes eid and name shall belong to the object
    def __init__(self, eid, name):
        print(">> self is:", self)
        self.eid = eid
        self.name = name

    def showEmployee(self):
        print(">> Employee:", self.eid, " | ", self.name)

# ContractEmployee IS CHILD OF Employee
class ContractEmployee(Employee): # IS-A Relation
    pass


"""
e1 = Employee(101, "John")
e1.showEmployee()

print(">> e1 is:",e1)

print("Employee Object pointed by e1 Contains:")
print(e1.__dict__)

print("Employee Class Contains:")
print(Employee.__dict__)
"""

print("Employee Class Contains:")
print(Employee.__dict__)

print()

print("ContractEmployee Class Contains:")
print(ContractEmployee.__dict__)

ce1 = ContractEmployee(111, "Fionna")
print("ContractEmployee Object pointed by ce1 Contains:")
print(ce1.__dict__)

ce1.showEmployee()

