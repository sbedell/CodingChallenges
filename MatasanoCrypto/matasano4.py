import binascii, string

# Matasano Crypto Challenges
# Challenge 4 - Detect single-character XOR

def singleCharXOR(s1, c):
    ans = str()
    for char in binascii.unhexlify(s1):
        ans += chr(c ^ char)
    return ans

def freqAnalysis(file):
    wordFreq = dict()
    with open(file) as f:
        for line in f:
            for word in line.split():
                cleanedWord = word.strip("();,?.\"").strip()
                if cleanedWord in wordFreq:
                    wordFreq[cleanedWord] += 1
                else:
                    wordFreq[cleanedWord] = 1
    words = list()
    for key in wordFreq.keys():
        # Tuning amount of times the word appears, filtering out single letters
        if wordFreq[key] > 5 and len(key) > 2:
            words.append(key.lower())
    return words

wordFreq = freqAnalysis("OriginOfSpecies.txt")
iceFreq = freqAnalysis("IceIce.txt")

with open("4.txt") as file:
    for line in file:
        # Iterate through all printable characters:
        for c in string.printable.encode():
            for word in singleCharXOR(line.strip("();,?.\"").strip().encode(), c).split():
                if word.strip("();,?.\"").strip() in iceFreq:
                    print("[!] Potential answer:", chr(c), "-", singleCharXOR(line.strip().encode(), c))

"""
[!] Answer: 5 - Now that the party is jumping
Prints out a ton of false positives though, bad word freq dict I guess...
"""
