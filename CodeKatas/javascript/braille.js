/**
 * CodaKatas - Translate a regular string to Braille.
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
    var plaintext = readLine();
    
    console.log(stringToBraille(plaintext));
}

function stringToBraille(text) {
    let brailleDict = new Map();
    brailleDict.set(' ', '000000');
    brailleDict.set('a', '100000');
    brailleDict.set('b', '110000');
    brailleDict.set('c', '100100');
    brailleDict.set('d', '100110');
    brailleDict.set('e', '100010');
    brailleDict.set('f', '110100');
    brailleDict.set('g', '110110');
    brailleDict.set('h', '110010');
    brailleDict.set('i', '010100');
    brailleDict.set('j', '010110');
    brailleDict.set('k', '101000');
    brailleDict.set('l', '111000');
    brailleDict.set('m', '101100');
    brailleDict.set('n', '101110');
    brailleDict.set('o', '101010');
    brailleDict.set('p', '111100');
    brailleDict.set('q', '111110');
    brailleDict.set('r', '111010');
    brailleDict.set('s', '011100');
    brailleDict.set('t', '011110');
    brailleDict.set('u', '101001');
    brailleDict.set('v', '111001');
    brailleDict.set('w', '010111');
    brailleDict.set('x', '101101');
    brailleDict.set('y', '101111');
    brailleDict.set('z', '101011');
    const CAPITAL_CODE = '000001';

    let finalBrailleCode = "";

    text.split("").forEach(function(char) {
        if (brailleDict.has(char)) {
            finalBrailleCode += brailleDict.get(char);
        } else if (brailleDict.has(char.toLowerCase())) {
            finalBrailleCode += CAPITAL_CODE;
            finalBrailleCode += brailleDict.get(char.toLowerCase());
        } else {
            console.error("Error, unexpected input");
        }
    });

    return finalBrailleCode;
}
