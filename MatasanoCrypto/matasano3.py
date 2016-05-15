import string, binascii
from cryptools import singleCharXOR, freqAnalysis

# Matasano Crypto Challenges
# Challenge 3 - Single-byte XOR cipher

hexstr = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print("Original = ", binascii.unhexlify(hexstr))

wordFreq = freqAnalysis("inputData/OriginOfSpecies.txt")

for c in string.printable.encode():
    for word in singleCharXOR(hexstr, c).split():
        if word.strip("();,?.\"").strip() in wordFreq:
            print("[!] Answer char =", chr(c), "->", singleCharXOR(hexstr, c))

"""
[!] Answer char = X -> Cooking MC's like a pound of bacon
"""
