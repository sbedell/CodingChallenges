function square(x) {
    return (x * x);
}

QUnit.module("Examples", () => {
    QUnit.test("Test tests", assert => {
        assert.ok(1 == "1", "Passed!" );
        assert.ok(1 === 1);
        assert.equal(1, "1");
        assert.notOk(1 === "1" , "triple equals");
    });

    QUnit.test("Test Square", assert => {
        assert.equal(square(2), 4, "square(2) == 4" );
    });

    QUnit.test("Test not square", assert => {
        assert.notEqual(square(2), 5, "square(2) != 5");
    });
});
