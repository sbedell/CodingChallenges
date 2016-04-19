import unittest
from primeFactors import getPrimeFactors, getPrimeFactorsRecursive

class TempKataTest(unittest.TestCase):
    def testPrimeFactors200(self):
        self.assertEqual([2, 5], getPrimeFactors(200))

    def testPrimeFactors10000000000(self):
        self.assertEqual([2, 5], getPrimeFactors(10000000000))

    def testPrimeFactors2500(self):
        self.assertEqual([2, 5], getPrimeFactors(2500))

    def testPrimeFactors2500(self):
        self.assertEqual([3, 11, 41, 271, 9091], getPrimeFactors(9999999999))

    def testPrimeFactors2500(self):
        self.assertEqual([3, 21649, 513239], getPrimeFactors(99999999999))

    def testLarge(self):
        self.assertEqual([2, 7, 41, 271, 9091], getPrimeFactors(9898989898))

    def testLarge2(self):
        self.assertEqual([3, 5, 17, 257, 65537], getPrimeFactors(4294967295))

    def testPrimeFactorsSame(self):
        self.assertEqual(getPrimeFactors(200), getPrimeFactors(10000000000))

    def testRecursive(self):
        self.assertEqual([2, 5], getPrimeFactorsRecursive(200, 2))

    def testRecursive2(self):
        self.assertEqual([2, 5], getPrimeFactorsRecursive(2500, 2))

    def testRecursive3(self):
        self.assertEqual([3, 5, 419], getPrimeFactorsRecursive(56565, 2))

    def testRecursive4(self):
        self.assertEqual([2, 3, 7, 13, 37], getPrimeFactorsRecursive(565656, 2))

    def testRecursive5(self):
        self.assertEqual([5, 41, 673], getPrimeFactorsRecursive(5656565, 2))

    def testRecursive6(self):
        self.assertEqual([2, 7, 73, 101, 137], getPrimeFactorsRecursive(56565656, 2))

    def testSameAlgos(self):
        self.assertEqual(getPrimeFactors(200), getPrimeFactorsRecursive(200, 2))

    def testNotSorted(self):
        self.assertNotEqual([5, 2], getPrimeFactors(200))

# -----------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
