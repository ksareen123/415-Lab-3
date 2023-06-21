# This is udpclient.py file

#Import socket programming module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Set destination port
port = 13000

# Include the server Address 
serverAddr = ('10.228.55.39', port)

# Send message. The string needs to be converted to bytes.
# To send more than one message, please create a loop
print("Type your message below")
message = input("->")
s.sendto(message.encode(), serverAddr)

# Receive no more than 1024 bytes
msg, addr = s.recvfrom(1024)
print("received: " + msg.decode())

# Close connection
s.close()
