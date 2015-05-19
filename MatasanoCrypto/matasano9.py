from cryptools import pkcs7

# Matasano Crypto Challenges
# Challenge 9 - PKCS#7 padding

given = b"YELLOW SUBMARINE"
expected = b"YELLOW SUBMARINE\x04\x04\x04\x04"

myAnswer = pkcs7(given, 20)
print( myAnswer )
assert(myAnswer == expected)
