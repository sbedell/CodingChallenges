// Test hashing of this own file

// Imports
const crypto = require('crypto');
const fs = require('fs');

const thisFilename = process.argv[1];
const hash = crypto.createHash('sha256');

const input = fs.createReadStream(thisFilename);
input.on('readable', () => {
  var data = input.read();
  if (data)
    hash.update(data);
  else {
    console.log(`The hash of the file ${thisFilename} is:`);
    console.log(`${hash.digest('hex')}`);
  }
});
