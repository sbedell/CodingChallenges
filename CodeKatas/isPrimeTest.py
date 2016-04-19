import unittest
from isPrime import isPrime

class TempKataTest(unittest.TestCase):
    def test2(self):
        self.assertTrue(isPrime(2), "2 is prime")

    def test3(self):
        self.assertTrue(isPrime(3), "3 is prime")

    def test9091(self):
        self.assertTrue(isPrime(9091), "9091 is prime")

    def test179(self):
        self.assertTrue(isPrime(179))

    def test277(self):
        self.assertTrue(isPrime(277))

    def testGoodLarge(self):
        self.assertTrue(isPrime(513239))

    def testBadCase(self):
        self.assertFalse(isPrime(4))

    def testBadLarge(self):
        self.assertFalse(isPrime(922337203685477))

    def testValueError_GivenNegativeNumber(self):
        with self.assertRaises(ValueError):
            isPrime(-5)

# -----------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
