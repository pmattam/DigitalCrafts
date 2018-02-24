// Flatten a nested array. You must account for varying levels of nesting.
// function steamrollArray(arr) {
//   // I'm a steamroller, baby
//   return arr;
// }

// steamrollArray([1, [2], [3, [[4]]]]);

// // prints out:

// [1,2,3,4]

var steamrollArray = function (list) {
    var convertedintoStr = list.join(",");
    var convertedintoArr = convertedintoStr.split(",");
    var newArray = [];
    for(i=0; i<convertedintoArr.length; i++) {
        newArray.push(parseInt(convertedintoArr[i]));
    }
    return newArray;
};

console.log(steamrollArray([[1, [2], [3, [[4]]]]]));