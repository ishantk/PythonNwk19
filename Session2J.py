routers = ["192.168.20.1", "192.168.20.2",
           "192.168.20.3", "192.168.20.4",
           "192.168.20.5","192.168.20.6", "192.168.20.7"]
# Indexing :   0                1               2               3               4,  5,  6

# Challenge: When the list of routers will increase so manually we have to write so much of code
# print(">> Router at 0 is on IP:", routers[0])
# print(">> Router at 1 is on IP:", routers[1])
# print(">> Router at 2 is on IP:", routers[2])
# print(">> Router at 3 is on IP:", routers[3])
# print(">> Router at 4 is on IP:", routers[4])

# for i in range(0, 5):                     # i : 0, 1, 2, 3, 4
# len is a built in function -> it will return the value as 5
for i in range(0, len(routers)):
    print(">> Router at", i, "is on IP:", routers[i])

print()

# Enhanced For Loop / For-Each Loop : Multi Value Containers
# Automatically data in the list will be copied into router one by one | 0 to n-1
# Strict Read Operation from 0 to n-1
for router in routers:
    print(">>", router)
    print(routers)
    print(">> :)")

# PS: Indexing works on Tuple and List :)


