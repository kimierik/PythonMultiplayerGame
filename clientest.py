from modules import client

client=client.client("localhost",9999,"utf_8")
msg=client.s.recv(1024).decode(client.proto)
print(msg)
