import sys, math

# Open up the file
try:
	ipInFile = open('euler8in', 'r')
except IOError as e:
	print ("Error when opening file " + str(ipAddrFile) + ". " + e.strerror + "\n" )
	sys.exit(-1)

# Read in the file
bigNum = ""
for line in ipInFile:
	bigNum += line.strip()
ipInFile.close()

dig1 = bigNum[0]
dig2 = bigNum[1]
dig3 = bigNum[2]
dig4 = bigNum[3]
dig5 = bigNum[4]
greatestProduct = int(dig1) * int(dig2) * int(dig3) * int(dig4) * int(dig5)
# Greatest product = 882 here

# Shift all down, get new greatest product
count = 5
for x in bigNum[5:]:
	#print x
	dig1 = dig2
	dig2 = dig3
	dig3 = dig4
	dig4 = dig5
	dig5 = bigNum[count]
	prod = int(dig1) * int(dig2) * int(dig3) * int(dig4) * int(dig5)
	if prod > greatestProduct:
		greatestProduct = prod
	count += 1

print ( greatestProduct )
