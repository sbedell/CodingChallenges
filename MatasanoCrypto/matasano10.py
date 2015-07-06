import base64
from Crypto.Cipher import AES
from Crypto import Random
from cryptools import fixedXorNoUnhex, splitArray

# ------------------------------------------
# Matasano Crypto Challenges
# Challenge 10 - Implement CBC Mode
# ------------------------------------------

def encryptCBC(plaintext, key, iv):
    """
    plaintext - text to cipher.
    key - AES keys can be 128, 192, or 256 bits long
    iv - your 16 bit IV
    # AES.block_size == 16
    """
    ecbCipher = AES.new(key, AES.MODE_ECB)
    splitText = splitArray(plaintext, AES.block_size)
    cipherText = ecbCipher.encrypt(fixedXorNoUnhex(splitText[0], iv))
    for i in range(1, len(splitText) - 1):
        cipherText += ecbCipher.encrypt(fixedXorNoUnhex(splitText[i], cipherText))
    return cipherText

def decryptCBC(ciphertext, key, iv):
    ecbCipher = AES.new(key, AES.MODE_ECB)
    splitText = splitArray(ciphertext, AES.block_size)
    plaintext = fixedXorNoUnhex(iv, ecbCipher.decrypt(splitText[0]))

    for i in range(1, len(splitText) - 1):
        plaintext += fixedXorNoUnhex(splitText[i-1], ecbCipher.decrypt(splitText[i]))
    return plaintext

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test Decrypting the given file:
theKey = b"YELLOW SUBMARINE"
iv = b"\x00" * AES.block_size

ciphertext = str()
with open("10.txt") as f:
    for line in f:
        ciphertext += base64.b64decode(line.strip())
# Len of plain cipher text = 3840
# Len of base64 decoded - len(ciphertext) = 2880

print(decryptCBC(ciphertext, theKey, iv))

# ~~~~~~~~~~~~~~~~~ Testing my own ~~~~~~~~~~~~~~~~~~~~~~~~
myKey = Random.new().read(AES.block_size)
myIV = Random.new().read(AES.block_size)
myString = b"TESTTESTTESTTEST"
cipher = AES.new(myKey, AES.MODE_CBC, myIV)
                                                    
encrypted = encryptCBC(myString, myKey, myIV)
#print(encrypted)
decrypted = decryptCBC(encrypted, myKey, myIV)
#print(decrypted)
assert(decrypted == myString)
print("Decryption algo working?", decrypted == myString)
