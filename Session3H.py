# String
# Textual Data (AlphaNumeric with Special Symbols)


companyName = 'Cisco'
# router = 'Cisco's ABC Router' #error
router = "Cisco's ABC Router"
anotherRouter = 'Cisco\'s XYZ Router'
myRouter = r'Cisco\'s PQR Router'       # Raw String

print(companyName)
print(router)
print(anotherRouter)
print(myRouter)

# For a bigger String we can divide it into multiple lines of code
message = "This is an Awesome Day. " \
          "We have learnt List and String. " \
          "Thank You !!"

print(message)


quotes = """
1. Be Exceptional
2. Work Hard, get Luckier
"""
print(quotes)