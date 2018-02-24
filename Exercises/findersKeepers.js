// Finders Keepers - higher order functions
// Write a function that accepts two parameters (you may add a third to differentiate type). 
// The first is an array, and the second is a function. 
// The function should look through the array for the first thing that matches the condition of the function passed. 
// If a match is not found, return false.
// Test at least these:

// findElement([1,3,5,8,9,10], function(num){return num % 2 === 0})
// Return 8
// findElement([1,3,5,9], function(num){return num % 2 === 0})
// Return false
// findElement['Jim','Indian','Marsh','Glitch'], function(str){return str.indexOf('itch) !== -1})
// Return Glitch

var findElement = function(arr, fn) {
    for(i=0; i<arr.length; i++) {
        if(fn(arr[i])) {
            return arr[i];
        }
    }
    return false;
};

console.log(findElement([1,3,5,8,9,10], function(num) {
    return num % 2 === 0;
}));
console.log(findElement([1,3,5,9], function(num) {
    return num % 2 === 0;
}));
console.log(findElement(['Jim','Indian','Marsh','Glitch'], function(str) {
    return str.indexOf('itch') !== -1;
}));
