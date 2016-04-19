// "translating" these from my python file
function isPrime(n) {
    if (n < 0) {
        throw "Error, cannot check negative numbers";
    }

    if (n % 2 == 0) {
        return (n == 2);
    }

    // Start at 3, go up to sqrt(n) + 1
    // step of 2 to only cycle thru odd numbers
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

function getPrimeFactors(num) {
    let primeFactors = new Set();
    let i = 2;

    while (num > 1) {
        while (num % i == 0) {
            primeFactors.add(i);
            num = parseInt(num / i);
        }
        i += 1
    }

    // Return sorted array of factors
    return Array.from(primeFactors).sort()
}
