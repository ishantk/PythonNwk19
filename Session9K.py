import paramiko as pk

sshClient = pk.SSHClient()
print(">> SSH Client Object Constructed")
sshClient.set_missing_host_key_policy(pk.AutoAddPolicy())
sshClient.connect(hostname="166.62.27.55", username="tech9", password="")
print(">> Connection Created")

stdin, stdout, stderr = sshClient.exec_command("ls")
print(stdin)
print(stdout)
print(stderr)