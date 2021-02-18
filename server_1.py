import socket
import datetime
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server: socket created")
host='192.168.1.6'
port=49152

server_socket.bind((host,port))
print("Server is ready!")

while True:
    data,addr=server_socket.recvfrom(4096)
    print("Message was succesfuly recieved from:{}".format(addr),"on: ",datetime.datetime.now())
    print("Server: Sending the Echo...")
    server_socket.sendto(data,addr)
    print("Echo was sent succesfully!")
    print("-------------------------------------------------------")

