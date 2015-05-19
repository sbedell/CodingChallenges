# Matasano Crypto Challenges
# Challenge 8 - Detect AES in ECB mode

import cryptotools

with open("8.txt") as f:
    for line in f:
        if cryptotools.ecbDetected(line.strip()):
            print("[!] Found ciphertext with repeating 16 byte blocks:")
            print(line.strip())
            print(cryptotools.splitArray(line.strip(), 16))
