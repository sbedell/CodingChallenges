// Test hashing of this own file

const crypto = require('crypto');
const fs = require('fs');

const thisFilename = process.argv[1];
const input = fs.createReadStream(thisFilename);

input.on('readable', function() {
  let hash = crypto.createHash('sha256');
  let data = input.read();

  if (data) {
    hash.update(data);
  } else {
    console.log(`The hash of this file ${thisFilename} is:`);
    console.log(`${hash.digest('hex')}`);
  }
});
