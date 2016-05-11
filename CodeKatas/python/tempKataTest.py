import unittest
from tempKata import getTempClosestToZero

class TempKataTest(unittest.TestCase):
    def testGetTempClosestToZero_GivenFile1(self):
        self.assertEqual(1, getTempClosestToZero("../testData/kataTemp1.txt"), "test message here")

    def testGetTempClosestToZero_GivenFile2(self):
        self.assertEqual(-5, getTempClosestToZero("../testData/kataTemp2.txt"))

    def testGetTempClosestToZero_GivenFile3(self):
        self.assertEqual(5, getTempClosestToZero("../testData/kataTemp3.txt"))

    def testGetTempClosestToZero_GivenFile4(self):
        self.assertEqual(5, getTempClosestToZero("../testData/kataTemp4.txt"))

    def testGetTempClosestToZero_GivenFile5(self):
        self.assertEqual(2, getTempClosestToZero("../testData/kataTemp5.txt"))

    def testGetTempClosestToZero_GivenFile6(self):
        self.assertEqual(0, getTempClosestToZero("../testData/kataTemp6.txt"))

    def testAssertionError1_GivenBadFile(self):
        with self.assertRaises(AssertionError):
            getTempClosestToZero("../testData/kataTempBadData.txt")

    def testAssertionError_GivenBadFile2(self):
        with self.assertRaises(AssertionError):
            getTempClosestToZero("../testData/badData2.txt")

    def testAssertionError_GivenBadFile3(self):
        with self.assertRaises(AssertionError):
            getTempClosestToZero("../testData/badData3.txt")

    def testIOError_GivenBadFile4(self):
        with self.assertRaises(IOError):
            getTempClosestToZero("thisDoesntExist.txt")

# -----------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
