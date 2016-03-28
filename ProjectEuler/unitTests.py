import unittest

from euler1 import sumOfMultiples
from euler2 import fibSequence
from euler3 import largestPrime, isPrime
from euler4 import isPalindrome, largestPalindrome
from euler6 import sumSquareDifference
from euler7 import findNthPrime
from euler9 import pythagTriplet
from euler10 import summationOfPrimes
from euler13 import largeSum
from euler14 import collatzChainLength
from euler16 import powerDigitSum
from euler20 import factorialDigitSum
from euler30 import digitFifthPowers
from euler39 import isRightTri
from euler40 import champConst
from euler48 import selfPowers

class EulerTests(unittest.TestCase):
    # Testing "helper" functions:

    def testIsPrime(self):
        self.assertTrue(isPrime(7))

    def testIsNotPrime(self):
        self.assertFalse(isPrime(10))
        
    def testPalindrome(self):
        self.assertTrue(isPalindrome('racecar'))

    def testNotPalindrome(self):
        self.assertFalse(isPalindrome('palindrome'))

    def testCollatz(self):
        self.assertEqual(collatzChainLength(13), 10)

    # Testing Euler Problems:
    def testEuler1(self):
        self.assertEqual(sumOfMultiples(3, 5), 233168)

    # SLOW
    # def testEuler2(self):
    #    self.assertEqual(fibSequence(4000000), 4613732)

    # SLOW
    # def testEuler3(self):
    #    self.assertEqual(largestPrime(600851475143), 6857)

    def testEuler4(self):
        self.assertEqual(largestPalindrome(1000), 906609)

    def testEuler6(self):
        self.assertEqual(sumSquareDifference(101), 25164150)

    # def testEuler7(self):
    #    self.assertEqual(findNthPrime(10001), 104743)

    # SLOW - adds about 20 seconds
    #def testEuler9(self):
    #   self.assertEqual(pythagTriplet(1000), 31875000)

    # SLOW 
    # def testEuler10(self):
    #   self.assertEqual(summationOfPrimes(2000001), 142913828922)
            
    # def testEuler13(self):
    #     Open file for reading:
    #     file_in = open('euler13infile', 'r')
    #     myLargeSum = largeSum(file_in)
    #
    #     self.assertEqual(myLargeSum[0:10], 5537376230)

    #def testEuler14(self):
    #    self.assertEqual(0, 837799)

    def testEuler16(self):
        self.assertEqual(powerDigitSum(1000), 1366)

    def testEuler20(self):
        self.assertEqual(factorialDigitSum(100), 648)

    def testEuler30(self):
        self.assertEqual(443839, digitFifthPowers(200000))

    # Correct - slow as hell
    # def testEuler40(self):
    #    self.assertEqual(champConst(), 210)
        
    # def testEuler48(self):
    #    self.assertEqual(str(selfPowers(1001))[-10:0], '9110846700')

if __name__ == '__main__':
    unittest.main()
