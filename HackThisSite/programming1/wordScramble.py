import sys, re

try:
    wordlist = open('wordlist.txt', 'r')
except IOError as e:
    print( "[!] Error opening file.\n[!] " + e.strerror )
    sys.exit(-1)

wordlist.close()

s = ('enogar lvelbyo elstla mjeyre'
    'uelacd '
    'rabbraa '
    'bbestka '
    'c1seehtr '
    'niamla '
    'dsmare ' )

print( "Wordlist opened and closed successfully." )
print ( s )
