function processData(input) {
    //Enter your code here
    
    // split string on newlines
    var splitInput = input.split("\n");
    
    var numStrings = parseInt(splitInput[0]);
    var strings = [];
    for (var i = 0; i < numStrings; i++) {
        strings.push(splitInput[i + 1]);   
    }
    
    var numQueries = splitInput[numStrings + 1];

    var queries = [];
    for (var i = 0; i < numQueries; i++) {
        queries.push(splitInput[i + numStrings + 2]);
    }
    
    queries.forEach(function(query) {
        var results = 0;
        strings.forEach(function(string) {
            if (query === string) {
                results++;
            }
        });
        console.log(results);
    });
}

processData("4\naba\nbaba\naba\nxzxb\n3\naba\nxzxb\nab");
