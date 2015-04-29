import string, binascii

# Matasano Crypto Challenges
# Challenge 3 - Single-byte XOR cipher

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
                if word in wordFreq:
                    wordFreq[word.strip().strip("();,?.\"")] += 1
                else:
                    wordFreq[word.strip().strip("();,?.\"")] = 1
    words = list()
    for word in wordFreq.keys():
        if wordFreq[word] > 25:   # tune this to whatever num you want
            words.append(word.lower())
    return words

hexstr = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print("Original = ", binascii.unhexlify(hexstr))

wordFreq = freqAnalysis("OriginOfSpecies.txt")

for c in string.printable.encode():
    for word in singleCharXOR(hexstr, c).split():
        if word.strip("();,?.\"").strip() in wordFreq:
            print("[!] Answer char =", chr(c), "->", singleCharXOR(hexstr, c))
