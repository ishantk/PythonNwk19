class Router:

    def __init__(self, rid, name, host, port):
        self.rid = rid
        self.name = name
        self.host = host
        self.port = port

    def toCSV(self):
        return "{}, {}, {}, {}\n".format(self.rid, self.name, self.host, self.port)


# r1 = Router(None, None, None, None)
#
# r1.rid = int(input(">> Enter Router ID"))
# r1.name = input(">> Enter Router Name")
# r1.host = input(">> Enter Router Host")
# r1.port = int(input(">> Enter Router Port"))

r1 = Router(1, "CISCO A", "198.127.12.12", 80)
r2 = Router(2, "CISCO B", "198.127.13.13", 80)
r3 = Router(3, "JUNIPER A", "198.127.14.14", 80)

print(r1.toCSV())
print(r2.toCSV())
print(r3.toCSV())

file = open("/Users/ishantkumar/Downloads/routers-nov.csv", "a")    # Append mode
file.write(r1.toCSV())
file.write(r2.toCSV())
file.write(r3.toCSV())

file.close()
print(">> Router Information Written...")
