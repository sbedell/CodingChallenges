## Project Euler 26
# Steve Bedell
# Answer: n = 983. This is the cycle:


from decimal import *

# Set decimal precision to 70 digits
getcontext().prec = 1500

longest = 1
answer = 0

# x.find(c)
def cycleLength(s):
	if len(s) < 2:
		return 0
	secondTwo = s[1:4] 	# actually 3 digigts
	#try:
	#except ValueError:
	index = s.find(secondTwo, 2)
	#for c in s:
	return index

for n in range(500, 1000):
	x = Decimal(Decimal(1) / Decimal(n))
	#print n, x
	splitX = str(x).split('.')		# splits on the decimal point
	#print splitX, type(splitX)
	decimals = splitX[1]
	print n, decimals
	clen = cycleLength(decimals)
	print clen
	print
	if clen > longest:
		longest = clen
		answer = n

print answer, longest
