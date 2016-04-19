// https://api.qunitjs.com/category/assert/
// https://api.qunitjs.com/expect/

const VERY_WEAK = "Very Weak";
const WEAK = "Weak";
const STRONG = "Strong";
const VERY_STRONG = "Very Strong";
const KINDA_STRONG = "Kinda Strong";

QUnit.module("Password Strength Tests", () => {
    QUnit.test("Test Very Weak", assert => {
        assert.equal(passwordStrength("123456"), VERY_WEAK, "123456 is very weak");
        assert.equal(passwordStrength("!!!"), "Very Weak - symbols only", "!!! is a really weak password");
    });

    QUnit.test("Test Weak", assert => {
        assert.equal(passwordStrength("weak"), WEAK, "'weak' is a weak password.");
    });

    QUnit.test("Test Strong", assert => {
        assert.equal(passwordStrength("OverEightChars1"), STRONG, "OverEightChars1 is strong.")
    });

    QUnit.test("Test Very Strong", assert => {
        assert.equal(passwordStrength("Chars1234@#$"), VERY_STRONG,
            "Chars1234@#$ is very strong.");
    });

    QUnit.test("Test Kinda Strong", assert => {
        assert.equal(passwordStrength("123456789"), KINDA_STRONG, "123456789 is kinda strong");
        assert.equal(passwordStrength("OverEightChars"), KINDA_STRONG);
        assert.equal(passwordStrength("#$%#$%#$%#$%#$%"), KINDA_STRONG);
    });
});
