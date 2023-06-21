#Used and edited by Krish Sareen

# This is udpserver.py file
import socket                                         

# create a UDP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Get local machine address
ip = "10.228.23.134"                          

# Set port number for this server
port = 13000                                          

# Bind to the port
serversocket.bind((ip, port))           

print("Waiting to receive message on port " + str(port) + '\n')

def xorcipher(plaintxt, key):
    ciphertext = ""
    txtciphertext = []

    for character in plaintxt:
        A = (ord(character))
        B = (ord(key))
        C = A^B
        ciphertext = ciphertext + chr(C)
        txtciphertext.append(hex(C))

    #print(plaintxt)
    #print(ciphertext)
    #print(txtciphertext)

    return ciphertext

while True:  
   xorkey = '&'
   # Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
   data, addr = serversocket.recvfrom(1024)
   print("received encrypted: " + data.decode())

   msg = data.decode()
   print("decrypted: " + xorcipher(msg, xorkey))

   print("Type your reply below")
   reply = input("->")  

   #encryptedreply = caesarencrypt(reply, caesarkey)
   encryptedreply = xorcipher(reply, xorkey)
   
   if (reply == "bye"):
      print("")
      print("Waiting to receive message on port " + str(port) + '\n')
      sent = serversocket.sendto(reply.encode(), addr)

   else:
      print('sent ' + encryptedreply)
      sent = serversocket.sendto(encryptedreply.encode(), addr)

   

