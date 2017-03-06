function main() {
  var numbers = "1 2 3 4 10 11";
  var arr = numbers.split(' ');
  arr = arr.map(Number);

  console.log(arraySum(arr));
}

function arraySum(numArr) {
  var sum = 0;
  
  numArr.forEach(function(item) {
      sum += Number(item);    
  });
  
  return sum;
}

main();