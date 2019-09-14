# String Formatting

name = "John"
profession = "Software Engr"
experience = 3

print("Welcome %s"%(name))
print("Good to know that you have %d years of experience as %s"%(experience, profession))

print()

print("Welcome", name)
print("Good to know that you have", experience, "years of experience as", profession)

print()

print("Welcome", name)
print("Good to know that you have", experience, "years of experience as", profession)

print()

print("Welcome {}".format(name))
print("Good to know that you have {} years of experience as {}".format(experience, profession))


number = 7

for i in range(1, 11):
    print("{} {}'s are {}".format(number, i, (number*i)))


