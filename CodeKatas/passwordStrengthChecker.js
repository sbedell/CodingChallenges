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
