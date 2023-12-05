import socket

#it should also be the same type of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to the server, mention the server's IP and port number
s.connect(('127.0.0.1', 55552))

#receive the message, specify the size of the message

message = s.recv(1024)

#print the message by decoding it
print(message.decode())
