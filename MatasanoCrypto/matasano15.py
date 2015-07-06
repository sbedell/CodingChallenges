import binascii
import base64
from cryptools import validatePKCS7, PaddingError

# ------------------------------------------
# Matasano Crypto Challenges
# Challenge 15 - PKCS#7 padding validation
# ------------------------------------------

good = b"ICE ICE BABY\x04\x04\x04\x04"
bad1 = b"ICE ICE BABY\x05\x05\x05\x05"
bad2 = b"ICE ICE BABY\x01\x02\x03\x04"

print(validatePKCS7(good))
assert(validatePKCS7(good) == b'ICE ICE BABY')

try:
    print(validatePKCS7(bad1))
except PaddingError:
    print("Padding Error occurred")
    
try:
    print(validatePKCS7(bad2))
except PaddingError:
    print("Padding Error occurred")
