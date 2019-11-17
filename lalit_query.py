file = open("demo.txt", "r")

fileContents = file.readlines()

for line in fileContents:
    # if line.__contains__("Cisco AP Name"):
    #     print(line)

    if line.startswith("Cisco AP Name"):
        print(line)

        # String API's to extract desired results
        words = line.split(" ")
        print(">> words: ", words)
        print(words[len(words)-1])




