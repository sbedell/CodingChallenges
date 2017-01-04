/**
 * Matasano Crypto Challenges
 * Challenge 7 - AES in ECB mode
 * 
 * This is currently NOT working correctly! :(
 */
"use strict";
const crypto = require('crypto');
const assert = require('assert');
const fs = require('fs');

// Start main part / Decryption
const theKey = "YELLOW SUBMARINE";

let ciphertextBuf = Buffer.from(fs.readFileSync('inputData/7.txt'), 'base64');

console.log(decryptAesEcb(ciphertextBuf, theKey));

/**
 * ciphertext - string to be decrypted.
 * key - string key, 16 bytes long.
 */
function decryptAesEcb(ciphertextBuffer, key) {
  const algorithm = 'aes-128-ecb';
  let decipher = crypto.createDecipher(algorithm, key);
  decipher.setAutoPadding(false);

  let deciphered = Buffer.concat([decipher.update(ciphertextBuffer), decipher.final()]);

  return deciphered.toString('base64');
}
