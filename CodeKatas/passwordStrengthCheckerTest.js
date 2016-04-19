QUnit.test("Hello test", assert => {
    assert.ok( 1 == "1", "Passed!" );
    assert.ok(1 === 1);
    assert.equal(1, "1");
    assert.notOk( 1 === "1" , "triple equals");
});

QUnit.test("Test Square", assert => {
    function square(x) {
        return (x * x);
    }
    assert.equal(square(2), 4, "square(2) == 4" );
});

QUnit.test("Test Very Weak", assert => {
    assert.equal(passwordStrength("123456"), "Very Weak", "123456 is very weak");
    assert.equal(passwordStrength("123456789", "Kinda Strong", "123456789 is kinda strong"))
});

QUnit.test("Test Kinda Strong", assert => {
    
});

// https://api.qunitjs.com/category/assert/
// https://api.qunitjs.com/expect/

// console.log(passwordStrength("123456789"));
// console.log(passwordStrength("weak")); // Weak
// console.log(passwordStrength("OverEightChars"));
// console.log(passwordStrength("OverEightChars1")); // Strong
// console.log(passwordStrength("Chars1234@#$")); // Very Strong
// console.log(passwordStrength("#$%#$%#$%#$%#$%"));
