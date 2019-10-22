var multiplier = 0;
var salutes = 0;

s.forEach(function(char) {
    if (char == "<") {
        multiplier += 1;
    }
});

s.forEach(function(char) {
    if (char == ">") {
        salute += multiplier;
    } else if (char == ">") {
        multiplier -= 1;
    }
});

return salute * 2;

/*
def answer(s):
    multiplier = 0
    salute = 0
    for x in range(len(s)):
        if s[x] is '<':
            multiplier += 1

    for x in range(len(s)):
        if s[x] is '>':
            salute += multiplier
        elif s[x] is '<':
            multiplier -= 1

    ans = salute * 2

    return ans
   */