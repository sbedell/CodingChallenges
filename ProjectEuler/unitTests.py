import unittest

from euler4 import isPalindrome, largestPalindrome
from euler6 import sumSquareDifference
from euler10 import summationOfPrimes, isPrime
from euler13 import largeSum
from euler20 import factorialDigitSum
from euler39 import isRightTri

class EulerTests(unittest.TestCase):
    # def setUp(self):
    #    """Setting up tests"""
    #
    # def testEuler13(self):
    #     Open file for reading:
    #     file_in = open('euler13infile', 'r')
    #     myLargeSum = largeSum(file_in)
    #
    #     self.assertEqual(myLargeSum[0:10], 5537376230)

    # def testEuler10(self):
        # answer = 142913828922

    # def testEuler6(self):
        # anwer =  25164150

    def testPalindrome(self):
        self.assertTrue(isPalindrome('racecar'))

    def testNotPalindrome(self):
        self.assertFalse(isPalindrome('palindrome'))

    def testEuler4(self):
        self.assertEqual(largestPalindrome(1000), 906609)

    def testEuler20(self):
        self.assertEqual(factorialDigitSum(100), 648)

if __name__ == '__main__':
    unittest.main()
