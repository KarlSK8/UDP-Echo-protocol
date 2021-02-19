import socket
import datetime
# Creating server socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server: socket created")
host='192.168.1.8' #IP address
port=49152 #Port number
#Bind socket
server_socket.bind((host,port))
print("Server is ready!")

while True:
    data,addr=server_socket.recvfrom(4096)
    print("Message was succesfuly recieved from:{}".format(addr),"on: ",datetime.datetime.now()) #When a message is received from a client, the server displays the address of this client and the date and time at which the message is received
    print("Server: Sending the Echo...")
    server_socket.sendto(data,addr) #Sending the echo back to the client
    print("Echo was sent succesfully!")
    print("-------------------------------------------------------")

