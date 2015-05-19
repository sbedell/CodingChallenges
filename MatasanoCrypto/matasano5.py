import binascii
from cryptools import repeatingXOR

# Matasano Crypto Challenges
# Challenge 5 - Implement repeating-key XOR

line1 = b"Burning 'em, if you ain't quick and nimble"
line2 = b"I go crazy when I hear a cymbal"
fullLine = line1 + "\n".encode() + line2

expected = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
key = b"ICE"

ans1 = repeatingXOR( line1, key)
ans2 = repeatingXOR( line2, key)
fullAns = repeatingXOR( fullLine, key)
print( "TheirCipher = ", expected)
print( "YourCipher  = ", fullAns)

# Verification: 
print( "\nCorrect?", fullAns == expected)
assert(fullAns == expected)
