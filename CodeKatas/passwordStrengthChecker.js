function passwordStrength(pw) {
    if (pw.length < 8) {
        if (pw.match(/\d+/)) {
            return "Very Weak";
        } else if (pw.match(/[a-zA-Z]+/)) {
            return "Weak";
        } else {
            return "Very Weak - symbols only";
        }
    } else {
        if (pw.match(/[A-Za-z0-9]+/) && pw.match(/\d+/) && pw.match(/[~!@#\$%\^&\*\(\)]+/)) {
            return "Very Strong";
        } else if (pw.match(/[A-Za-z]+/) && pw.match(/\d+/)) {
            return "Strong";
        } else {
            return "Kinda Strong";
        }
    }
}
