function passwordStrength(pass) {
    if (pass.length < 8) {
        if (pass.match(/\d+/)) {
            return "Very Weak";
        } else if (pass.match(/[a-zA-Z]+/)) {
            return "Weak";
        }
    } else {
        if (pass.match(/[A-Za-z]+/) && pass.match(/\d+/) && pass.match(/[~!@#\$%\^&\*\(\)]+/)) {
            return "Very Strong";
        } else if (pass.match(/[A-Za-z]+/) && pass.match(/\d+/)) {
            return "Strong";
        } else {
            return "Kinda Strong";
        }
    }
}

console.log(passwordStrength("123456")); // Very Weak
console.log(passwordStrength("123456789"));
console.log(passwordStrength("weak")); // Weak
console.log(passwordStrength("OverEightChars"));
console.log(passwordStrength("OverEightChars1")); // Strong
console.log(passwordStrength("Chars1234@#$")); // Very Strong
console.log(passwordStrength("#$%#$%#$%#$%#$%"));