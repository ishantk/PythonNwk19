import telnetlib

HOST = "www.auribises.com"
PORT = 80

# Create a Telnet Object
tn = telnetlib.Telnet(HOST, PORT)
print(">> tn is:", tn)

message = ("GET /index.html HTTP/1.1\nHost:"+HOST+"\n\n").encode("ascii")
tn.write(message)
print(">> Message Written")

output = tn.read_all()
print(">> Output:", output)


