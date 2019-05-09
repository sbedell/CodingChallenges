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
    var total_lambs = parseInt(readLine());
    
    if (total_lambs < 10 || total_lambs > Math.pow(10,9)) {
        console.error("Error - total lambs should be between 10 and 10^9");
    } else {
        console.log(answer(total_lambs));
        //console.log(findGenerousPay(total_lambs));
        //console.log(findStingyPay(total_lambs));
    }
}

function answer(totalLambs) {
    return (findStingyPay(totalLambs) - findGenerousPay(totalLambs));
}

// Using a fibonacci sequence, this is working
function findStingyPay(totalLambs) {
    var totalPaid = 0;
    var lambAllowance = 1;
    var previousLambAllowance1 = 0;
    var previousLambAllowance2 = 1; 

    while (totalLambs >= lambAllowance) {
        //console.log("total lambs: " + totalLambs);
        //console.log("Previous allowance: " + previousLambAllowance2);
        //console.log("Current allowance:" + lambAllowance);
        
        totalLambs -= lambAllowance;
        
        lambAllowance = previousLambAllowance1 + previousLambAllowance2;
        previousLambAllowance1 = previousLambAllowance2;
        previousLambAllowance2 = lambAllowance;
       
        totalPaid++;
    }
    
    return totalPaid;
}

// Working correctly, just using simple doubling
function findGenerousPay(totalLambs) {
    var totalPaid = 0;
    var lambAllowance = 1;
    
    while (totalLambs >= lambAllowance) {
        totalLambs -= lambAllowance;
        lambAllowance = lambAllowance * 2;
        totalPaid++;
    }
    
    return totalPaid;
}
