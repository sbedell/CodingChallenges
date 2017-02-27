// Python
/*
import math

def isPrime(n):
    if (n % 2 == 0):
        return (n == 2)

    # start at 3, go up to sqrt(n) + 1
    # step of 2 to only cycle thru odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            return False
    return True
*/

function isPrime(n) {
    if (n % 2 == 0) return (n == 2);

    // start at 3, go up to sqrt(n) + 1
    // step of 2 to only cycle thru odd numbers
    for (let i = 3; i < Math.sqrt(n); i + 2) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

console.log(isPrime(2));
console.log(isPrime(4));