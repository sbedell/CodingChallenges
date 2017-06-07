/**
 * CodaKatas - Minion Hierarchy Challenge
 * 
 * All of this until "ignore above this line" is from the initial code skeleton
 */ 
process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
  var x = parseInt(readLine());
  
  if (x >= 0 && x <= 10) {
    console.log(answer(x));
  } else {
    console.error("Input needs to be between 0 and 10");
  }
}

function answer(x) {
  if (x === 1) {
      return 8;
  } else { 
      return Math.pow(7, x) + answer(x - 1);
  }
}