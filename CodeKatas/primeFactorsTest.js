QUnit.module("Prime Factors tests", () => {
    QUnit.test("isPrime", assert => {
        assert.ok(isPrime(2));
        assert.ok(isPrime(277));
    });

    QUnit.test("Not Prime", assert => {
        assert.notOk(isPrime(4));
        assert.notOk(isPrime(250));
        assert.notOk(isPrime(Number.MAX_SAFE_INTEGER), "Max Safe Int is not prime")
        // assert.throws(isPrime(-5), "Error, cannot check negative numbers", "throws error");
    });

    QUnit.test("Prime Factors", assert => {
        assert.deepEqual([2, 5], getPrimeFactors(200));
        assert.deepEqual([2, 5], getPrimeFactors(10000000000));
        assert.notDeepEqual([5, 2], getPrimeFactors(200));
    });
});
