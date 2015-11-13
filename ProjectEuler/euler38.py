# Project Euler problem 38
# Not passing on projecteuler.net

def isPandigital(n):
	"""
	Checks if a number is pandigital.
	i.e. contains all the digits:
		1 2 3 4 5 6 7 8 9
	"""
	if len(n) != 9:	return False
	for x in range(1, 10): 		#ints?
		if not str(x) in str(n):
			return False
	return True					# Else case, essentially

# -------------------------------------------
# Main Method
if __name__ == '__main__':
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
