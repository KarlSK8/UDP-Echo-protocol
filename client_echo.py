import socket
import timeit
RTT_=[]
#Create socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Client: socket created")
host=input("Enter IP address: ") #Take IP address as input
port=input("Enter port number: ") #take port number as input
print("-------------------------------------------------")
message="THIS IS ECHO " #the message to be sent to the server
for i in range(5):
    message_=message+str(i+1)
    print("Client: "+message_)
    t0=timeit.default_timer() #time at which the message is sent
    client_socket.sendto(message_.encode(),(host,49152)) #sending the message to the desired address
    data,server=client_socket.recvfrom(4096)
    t1=timeit.default_timer() #time at which the echo was received
    data=data.decode() #decoding the echo and then print it.
    print("Server: "+data)
    print("RTT= ",(t1-t0)*1000, "ms") #difference between t1 and t0 is equal to the round trip time
    print("-------------------------------------------------")
    RTT=(t1-t0)*1000
    RTT_.append(RTT) #append the RTT to the list to use it later in the average RTT calculation
sum_of_rtt=0
#This loop serves to add all the RTT inside the list
for j in range(len(RTT_)):
    sum_of_rtt=(float(RTT_[j])+sum_of_rtt)
#The average round trip time is the sum of RTT's divided by the number of RTT's
print("Average Round Trip Time= ",sum_of_rtt/(j+1), "ms")
print("-------------------------------------------------")
print("Closing socket...")
print("-------------------------------------------------")
client_socket.close()
        
    
