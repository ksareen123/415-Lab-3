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