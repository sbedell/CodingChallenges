import cryptools

# Matasano Crypto Challenges
# Challenge 8 - Detect AES in ECB mode
with open("inputData/8.txt") as f:
    for line in f:
        if cryptools.ecbDetected(line.strip()):
            print("\n[!] Found ciphertext with repeating 16 byte blocks:")
            print(line.strip() + "\n")
            print(cryptools.splitArray(line.strip(), 16))
