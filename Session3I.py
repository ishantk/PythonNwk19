name = "John Watson"
print(name, type(name), hex(id(name)))

print()

anotherName = "John Watson"
print(anotherName, type(anotherName), hex(id(anotherName)))

# name and anotherName are Reference Variables which holds HashCode of John Watson as data :)

print("Length of Name is:", len(name)) # 11
print("Max of Name is:", max(name))    # t
print("Min of Name is:", min(name))    # empty space

print(name[1])                  # o
print(name[len(name)-1])        # n

print(name[1:4])                # ohn

print("hn" in name)

email = input("Enter an Email: ")

if "@" in email and ".com" in email:
    print(">> A Valid Email")
else:
    print("Its an Invalid Email")

