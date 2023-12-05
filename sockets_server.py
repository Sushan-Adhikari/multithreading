import socket

#what kind of socket we want?
#what  kind of protocol do we want? 
#which IP  we wanna host the server on?
#which port would we be using? Don't use the reserved ports

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#we specifined the kind of socket: internet socket and the type of protocol
#for UDP it would be SOCK_DGRAM
s.bind(('127.0.0.1', 55552))    #the host and port for this socket to run on

s.listen()

#endless loop that accepts the connection
while True:
    client, address = s.accept()    #we get a client in return
    print("connected to {}".format(address))
    client.send("You are connected via a socket".encode())
    client.close()
