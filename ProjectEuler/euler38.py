# Project Euler problem 38

"""
Checks if a number is pandigital.
i.e. contains all the digits:
	1 2 3 4 5 6 7 8 9
"""
def isPandigital(n):
	if len(n) != 9:	return False
	for x in range(1, 10): 		#ints?
		if not str(x) in str(n):
			return False
	return True					# Else case, essentially

# -------------------------------

largest = 918273645

for i in range(5000, 10000):
	num = ""
	for n in range(20000, 50000):
		num += str(i * n)
		#print num, isPandigital(num)
		if isPandigital(num):
			if num > largest:
				largest = num

print "\nLargst num = " + str(largest)
