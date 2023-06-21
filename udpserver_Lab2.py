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

def caesarencrypt(msg, shift):
    ciphertext = ""
    for symbol in msg:
        #print(letter, symbol)
        asciival = ord(symbol)
        #print(asciival)
        asciival = (asciival + shift) % 128
        #print(asciival)
        ciphertext = ciphertext + chr(asciival)
        #print(ciphertext)

    return ciphertext

def caesardecrypt(msg, shift):
    plaintxt = ""
    for symbol in msg:
        #print(letter, symbol)
        asciival = ord(symbol)
        #print(asciival)
        asciival = (asciival - shift) % 128
        #print(asciival)
        plaintxt = plaintxt + chr(asciival)
        #print(ciphertext)

    return plaintxt

def xorcipher(plaintxt, key):
    ciphertext = []
    txtciphertext = []

    for character in plaintxt:
        A = (ord(character))
        B = (ord(key))
        C = 0
        C = A^B
        ciphertext.append(C)
        txtciphertext.append(hex(C))

    #print(plaintxt)
    #print(ciphertext)
    #print(txtciphertext)

    return ciphertext

while True:  
   
   caesarkey = 4
   xorkey = 'k'
   # Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
   data, addr = serversocket.recvfrom(1024)
   print("received encrypted: " + data.decode())

   msg = data.decode()
   print("decrypted: " + caesardecrypt(msg, caesarkey))

   print("Type your reply below")
   reply = input("->")  

   encryptedreply = caesarencrypt(reply, caesarkey)
   #encrytpedreply = xorcipher(reply, xorkey)
   
   if (reply == "bye"):
      print("")
      print("Waiting to receive message on port " + str(port) + '\n')
      sent = serversocket.sendto(reply.encode(), addr)

   else:
      print('sent ' + encryptedreply)
      sent = serversocket.sendto(encryptedreply.encode(), addr)

   

