# Normal/Regular if/else
transmissionDelay = 120
if transmissionDelay >= 60:
    print(">> Performance Tuning Required")
    # Anything which must be executed under if block should be 4 spaces inwards
    # 4 spaces -> 1 tab space
else:
    print(">> All OK !!")
    # Anything which must be executed under else block should be 4 spaces inwards
    # 4 spaces -> 1 tab space

# PEP Standard : Python Enhancement Proposal

# Nested if/else
isInternetEnabled = False
isGPSEnabled = False

print()

if isInternetEnabled:
    if isGPSEnabled:
        print(">> You can Navigate using Google Maps")
    else:
        print(">> Turn On GPS and Try Again !!")
else:
    print(">> Turn On Internet and Try Again !!")

print()

username = input("Enter Username:")
password = input("Enter Password:")

if username == "john@example.com" and password == "password123": # Hard Code Check
    print(">> UserName and Password OK")
    print(">> Welcome to Home")
else:
    print(">> Invalid UserName or Password")

print()

# Ladder if/else
# 1 : SuperAdmin
# 2 : Admin
# 3 : User

userType = int(input("Select Your Role as a User"))

if userType == 1:
    print(">> Welcome Home, Super Admin")
elif userType == 2:
    print(">> Welcome Home, Admin")
elif userType == 3:
    print(">> Welcome Home, User")
else:
    print(">> Invalid User Type")


