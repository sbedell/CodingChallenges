import binascii, base64
from Crypto.Cipher import AES

# Using Python 2.7 because I could only install PyCrypto on 2.7
# Matasano Crypto Challenges
# Challenge 7 - AES in ECB mode

def aesDecryptECB(ciphertext, key):
    """
    ciphertext = string to be decrypted
    key = string key, 16 bytes long plz
    """
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

# --- Main / Decrypt ----

theKey = "YELLOW SUBMARINE"

ciphertext = str()
with open("7.txt") as f:
    for line in f:
        ciphertext += base64.b64decode(line.strip())

# print(ciphertext)
try:
    print(aesDecryptECB(ciphertext, theKey))
except ValueError:
    print("Value Error, likely odd length string")
