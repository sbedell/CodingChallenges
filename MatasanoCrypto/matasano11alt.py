import os
import random
from Crypto.Cipher import AES
from cryptools import ecbDetected, splitArray, fixedXorNoUnhex

# ------------------------------------------
# Matasano Crypto Challenges
# Challenge 11 - ECB/CBC detection oracle
# ------------------------------------------

# Taken from challenge 9:
def paddingPKCS7(s, n):
    '''
    s - string to pad
    n - blocksize to pad UP TO
    '''
    amtToPad = n - len(s)
    return s + bytearray([amtToPad] * amtToPad)

# Taken from Challenge 10
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
    """
    Encrypts randomly ECB or CBC
    Puts 5-10 length padding before and after
    """
    randAesKey = os.urandom(AES.block_size)
    randBytes1 = os.urandom(random.randint(5, 10))
    randBytes2 = os.urandom(random.randint(5, 10))
    appendedText = randBytes1 + plaintext + randBytes2
    
    if round(random.randint(0, 1)) == 1:
        print("Encrypting using ECB")
        cipher = AES.new(randAesKey, AES.MODE_ECB)
        
        # Need to pad to a multiple of 16 bytes
        if len(appendedText) % 16 != 0:
            print("len = ", len(appendedText) % 16)
            remainder = 16 - (len(appendedText) % 16)
        pkcsText = paddingPKCS7(appendedText, len(appendedText) + remainder)
        print("PKCS = ", pkcsText.decode(), len(pkcsText.decode()))
        return cipher.encrypt(pkcsText.decode())
    else:
        print("Encrypting using CBC")
        randIV = os.urandom(AES.block_size)
        return encryptCBC(appendedText, randAesKey, randIV)

def encryptionOracle(text):
    if (ecbDetected(text)):
        return "ECB"
    else:
        return "CBC"

# ~~~~~~~~~~~~~~~~~~~~~~~ TESTING ~~~~~~~~~~~~~~~~~~~~
myString = b"TESTTESTTESTTEST"

for i in range(10):
    try:
        encryptedText = randomEncryptEcbCbc(myString)
        print("Encryption Oracle says " + str(encryptionOracle(encryptedText)))
        print('\n')
    except ValueError:
        print("Error, not a multiple of 16, cannot encrypt\n")
