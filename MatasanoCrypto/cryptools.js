const crypto = require('crypto');

// list available ciphers:
const ciphers = crypto.getCiphers();
console.log("\nCiphers: ");
console.log(ciphers); // ['aes-128-cbc', 'aes-128-ccm', ...]

// list available hash functions:
const hashes = crypto.getHashes();
console.log("\nHash functions: ")
console.log(hashes); // ['DSA', 'DSA-SHA', 'DSA-SHA1', ...]

// list available elliptic curves:
const curves = crypto.getCurves();
console.log("\n Elliptic curves: ");
console.log(curves); // ['Oakley-EC2N-3', 'Oakley-EC2N-4', ...]

// list crypto constants / defaults:
console.log("\n");
console.log(crypto.constants.defaultCoreCipherList);
console.log("\n");
console.log(crypto.constants.defaultCipherList);

// PKCS Stuff:
// def paddingPKCS7(s, n):
//     amtToPad = n - len(s)
//     return s + bytes([amtToPad] * amtToPad)
/**
 * 
 * @param {String} str - string to pad 
 * @param {int} n - blocksize to pad UP TO 
 */
function paddingPKCS7(str, n) {
    let amountToPad = n - str.length;
    console.log(amountToPad);

    return str; // god dammit
}