function numCamelCaseWords(str) {
    var numWords = 1;
    
    str.split("").forEach(function(char) {
       if (char === char.toUpperCase()) {
         numWords++;       
       }
    });
    
    return numWords;
}

console.log(numCamelCaseWords("saevChangesInTheEditor"));
console.log(numCamelCaseWords("testMe")); 
console.log(numCamelCaseWords("test"));