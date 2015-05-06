# Matasano Crypto Challenges
# Challenge 8 - Detect AES in ECB mode

def splitArray(array, n):
    """ array - an array or string to be split into a list
        n - length of the chunks
    """
    return [array[i:i+n] for i in range(0, len(array), n)]

def ecbDetected(ciphertext):
    """
    Returns true if there are repeating 16 byte chunks
    Returns false otherwise.
    ciphertext = text to check
    """
    chunkedText = splitArray(ciphertext, 16)
    repeatedBlocks = dict()
    for chunk in chunkedText:
        repeatedBlocks[chunk] = 1
    return len(repeatedBlocks) < len(chunkedText)

with open("8.txt") as f:
    for line in f:
        if ecbDetected(line.strip()):
            print("[!] Found ciphertext with repeating 16 byte blocks:")
            print(line.strip())
            print(splitArray(line.strip(), 16))
