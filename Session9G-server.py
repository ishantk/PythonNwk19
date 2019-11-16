# SERVER PROGRAM
# import socket
import socket as sk

# Create a Socket Object
s = sk.socket()
print(">> Socket Object Constructed")

# Mention Some Port number, where your server will run
port = 12348

# bind is a function to listen to port number from an ip
# we can listen from any ip
s.bind(('', port))
print(">> Binding Done for Port#", port)

s.listen(5)
print(">> Listening Started")

# Infinite Loop Running in our Server Program
while True:
    # if some client sends us the request, we shall accept it
    cl, addr = s.accept()
    print(">> Got a Connection Requested from", addr)

    # Send the message back to client with send function
    cl.send(b"Thank You for Connecting with Us!!")  # b means data will be transmitted as bytes

    cl.close()   # Close the Connection