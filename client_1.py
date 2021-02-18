import socket
import timeit
RTT_=[]
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client: socket created")
host=input("Enter IP address: ")
port=input("Enter port number: ")
print("-------------------------------------------------")
message="THIS IS ECHO "
for i in range(5):
    message_=message+str(i+1)
    print("Client: "+message_)
    t0=timeit.default_timer()
    client_socket.sendto(message_.encode(),(host,49152))
    data,server=client_socket.recvfrom(4096)
    t1=timeit.default_timer()
    data=data.decode()
    print("Server: "+data)
    print("RTT= ",(t1-t0)*1000, "ms")
    print("-------------------------------------------------")
    RTT=(t1-t0)*1000
    RTT_.append(RTT)
sum_of_rtt=0  
for j in range(len(RTT_)):
    sum_of_rtt=(float(RTT_[j])+sum_of_rtt)
print("Average Round Trip Time= ",sum_of_rtt/(j+1), "ms")
print("-------------------------------------------------")
print("Closing socket...")
print
print("-------------------------------------------------")
client_socket.close()
        
    
