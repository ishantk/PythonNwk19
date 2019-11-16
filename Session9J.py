# We are only doing an Import for ConnectHandler class

from netmiko import ConnectHandler

cisco = {
    "device_type": "cisco_ios",
    "host": "cisco.domain.com",
    "username": "admin",
    "password": "cisco123"
}

print(cisco)
print(type(cisco))

netConnect = ConnectHandler(**cisco) # We are creating a Connection
print(netConnect) # show us the HashCode of ConnectHandler Object

# netConnect = ConnectHandler(device_type="cisco_ios",
#     host="cisco.domain.com",
#     username="admin",
#     password="cisco123")

print(">> Connected")

prompt = netConnect.find_prompt()
print(">> Prompt:", prompt)

output = netConnect.send_command("show ip int brief")
print(">> Output")
print(output)

# https://pynet.twb-tech.com/blog/automation/netmiko.html

