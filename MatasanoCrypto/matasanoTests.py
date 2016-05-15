import unittest
import binascii
import cryptools
# --------------------------------------------

class TempKataTest(unittest.TestCase):
    # Matasano 1
    def testHexToBase64(self):
        hexstr = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

        self.assertEquals(expected, cryptools.hexToBase64(hexstr))

    # Matasano 2
    def testFixedXOR(self):
        buf1 = b"1c0111001f010100061a024b53535009181c"
        buf2 = b"686974207468652062756c6c277320657965"
        expected = b"746865206b696420646f6e277420706c6179"
        ans = cryptools.fixedXOR(buf1, buf2)
        hexans = binascii.hexlify(ans.encode())
        self.assertEquals(expected, hexans)

    def testMatasano5(self):
        line1 = b"Burning 'em, if you ain't quick and nimble"
        line2 = b"I go crazy when I hear a cymbal"
        fullLine = line1 + "\n".encode() + line2
        expected = b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        key = b"ICE"

        fullAns = cryptools.repeatingXOR(fullLine, key)
        self.assertEquals(fullAns, expected)

# -----------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
