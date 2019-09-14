ipAddresses = []
choice = "yes"

while choice == "yes":
    ipAddress = input("Enter IP Address: ")
    ipAddresses.append(ipAddress)

    choice = input("Would You Like to add another IP Address (yes/no): ")


print(ipAddresses)
print(">> You have entered:", len(ipAddresses), "IP Addresses")
