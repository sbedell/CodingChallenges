import os, random
from Crypto.Cipher import AES
from cryptools import ecbDetected, splitArray, fixedXorNoUnhex, paddingPKCS7

# ------------------------------------------
# Matasano Crypto Challenges
# Challenge 11 - ECB/CBC detection oracle
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

def randomEncryptEcbCbc(plaintext):
    randAesKey = os.urandom(AES.block_size)
    randBytes = os.urandom(random.randrange(5, 11))
    paddedText = randBytes + plaintext + randBytes
    
    if round(random.randrange(1, 3)) == 1:
        print("ECB")
        cipher = AES.new(randAesKey, AES.MODE_ECB)
        
        # Need to somehow pad to a multiple of 16 bytes
        #if paddedText % 16 != 0:
        #    remainder = paddedText / 16
            
        return cipher.encrypt(paddedText)
    elif round(random.randrange(1, 3)) == 2:
        print("CBC")
        randIV = os.urandom(AES.block_size)
        return encryptCBC(paddedText, randAesKey, randIV)

def encryptionOracle(text):
    if (ecbDetected(text)):
        return "ECB"
    else:
        return "FUCKKKKKKSALT"

# ~~~~~~~~~~~~~~~~~~~~~~~ TESTING ~~~~~~~~~~~~~~~~~~~~
myString = b"TESTTESTTESTTEST"

print(randomEncryptEcbCbc(myString))
print(randomEncryptEcbCbc(myString))
print(randomEncryptEcbCbc(myString))
print(randomEncryptEcbCbc(myString))
print(randomEncryptEcbCbc(myString))
