import socket as sk

s = sk.socket()
print(">> Socket Object Constructed")

port = 12348

s.connect(("127.0.0.1", port))
print(">> Connection Requested to Server")

print(">> Data Received from Server")
print(s.recv(1024))

s.close()
print(">> Connection Closed by Client")

