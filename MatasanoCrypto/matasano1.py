import binascii
from cryptools import hexToBase64

# Matasano Crypto Challenges
# Challenge 1 - Convert hex to base64

hexstr = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Print the original message 4 fun:
print(binascii.unhexlify(hexstr))

print("Answer   = ", hexToBase64(hexstr))
print("Expected = ", expected)
print("Correct? ", expected == hexToBase64(hexstr))
assert(expected == hexToBase64(hexstr))

# This works too, just a test
print(binascii.b2a_base64(binascii.unhexlify(hexstr)))
