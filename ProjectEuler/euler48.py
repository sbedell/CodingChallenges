totalSum = 0

for n in range(1, 1001): # actually 1 - 10
	totalSum += int(n**n)

print totalSum
print "\n"
print str(totalSum)[-10:]
