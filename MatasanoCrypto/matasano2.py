import binascii
from cryptools import fixedXOR

# Matasano Crypto Challenges
# Challenge 2 - Fixed XOR

buf1     = b"1c0111001f010100061a024b53535009181c"
buf2     = b"686974207468652062756c6c277320657965"
expected = b"746865206b696420646f6e277420706c6179"

# Printing messages for fun. Type - <class 'bytes'>
print("unhex 1 = ", binascii.unhexlify(buf1) )
print("unhex 2 = ", binascii.unhexlify(buf2), "\n")

ans = fixedXOR(buf1, buf2)
hexans = binascii.hexlify(ans.encode())

print( "Expected  XOR =", binascii.unhexlify(expected))
print( "My Answer XOR =", ans.encode(), "\n")

print( "Expected  hex =", expected)
print( "My Answer hex =", hexans , "\n")

print("Correct? ", expected == hexans)
assert(expected == hexans)
