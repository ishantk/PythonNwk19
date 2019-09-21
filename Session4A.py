quote = "work hard and get luckier"
# Converting String into list
# list of alphabets
# MUTABLE
data = list(quote)
print(data)

# IMMUTABLE
data = tuple(quote)
print(data)

data = set(quote) # No Duplicate alphabets will come up
print(data)

print(quote * 2)   # ?
print(quote[::-1]) # Reverse of String

count = 0
for i in range(0, len(quote)):
    print(quote[i], end="-")
    if quote[i] == 'r':
        count = count + 1

print()
print(">> r count is:", count)

print()
print(len(quote)) # 25

                # 24 , 0 i.e. less than -1, -1 (to decrement by -1)
for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")
