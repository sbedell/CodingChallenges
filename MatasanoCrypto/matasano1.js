"use strict";
const assert = require('assert');

let hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
let expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";

// print original message for fun:
let unhexed = Buffer.from(hexstr, "hex");
console.log("\n" + unhexed.toString() + "\n");

let unhexedBase64 = base64Encode(unhexed);
console.log(`My Answer: ${unhexedBase64}`);
console.log(`Expected:  ${expected}`);

assert.equal(unhexedBase64, expected);

function base64Encode(string) {
  return Buffer.from(string).toString('base64');
}
