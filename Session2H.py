ipAddress = input(">> Enter an IP Address: ")
print(">> You Entered:", ipAddress)

# Class B : 128.0.0.0 to 191.255.255.255
# Class C : 192.0.0.0 to 223.255.255.255

# Slicing : 0:3 means begin from 0th index till 2nd index
firstThreeChars = ipAddress[0:3]
print(">> Your First Three Characters are:")
print(">> firstThreeChars is:", firstThreeChars, type(firstThreeChars))

# Whatever we are giving as an input on console is always a string
# we need to convert textual i.e. string data into corresponding mathematical type

# Converting str to int
number = int(firstThreeChars)

print(">> number is:", number, type(number))

if number >=128 and number <=191:
    print(">>", ipAddress, " is Class B IP Address")
elif number >=192 and number <=223:
    print(">>", ipAddress, " is Class C IP Address")
else:
    print(">> Invalid IPAddress as per our Requirements")

# Assignment: Finish off the above program gracefully !!





