import math

"""
	Tests if a, b, c "pass" the
	Pythagorean Theorem
"""
def isRightTri(a, b, c):
	summ = int(math.pow(a, 2)) + int(math.pow(b, 2))
	csquare = int(math.pow(c, 2))
	return summ == csquare

print isRightTri(30, 40, 50)
print isRightTri(1, 2, 5)
