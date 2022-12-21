// floodFill(canvas, x, y, target)
// canvas is an array of array of numbers representing
// colored pixels (think MSPaint)
// x, y is your start point, target is your new "color"
// change the value at x, y on the canvas to
// the target value, then all points on the canvas 
// that were the original color and contiguous with the 
// point at x, y (no diagonals!) to the target color.
//
// example, if canvas is:
// [[3, 2, 4, 4, 4],
//  [4, 4, 4, 3, 3],
//  [4, 1, 1, 4, 4]]
// x, y is 2, 1  and target is 0
// canvas becomes:
// [[3, 2, 0, 0, 0],
//  [0, 0, 0, 3, 3],
//  [0, 1, 1, 4, 4]]
//
// another example, if canvas is:
// [[1, 0, 2, 0, 1],
//  [1, 0, 1, 1, 0],
//  [1, 0, 1, 0, 0],
//  [2, 0, 0, 2, 1]]
// x, y is 1, 2 and target is 9
// canvas becomes:
// [[1, 9, 2, 0, 1],
//  [1, 9, 1, 1, 0],
//  [1, 9, 1, 0, 0],
//  [2, 9, 9, 2, 1]]
// if x, y was intead 2, 1 and target was 9
// canvas would become:
// [[1, 0, 2, 0, 1],
//  [1, 0, 9, 9, 0],
//  [1, 0, 9, 0, 0],
//  [2, 0, 0, 2, 1]]
// you don't need to return anything,
// but if you feel the need to, use null or undefined
// make sure you don't modify anything outside your canvas area


// function floodFill(canvas, x, y, target) {
//     for( x; i)
// }

// var sample_input = [[1, 0, 1, 1, 1],
//                     [0, 1, 1, 1, 0],
//                     [1, 0, 1, 0, 0]]
// floodFill(sample_input, 1, 1, 9)

// console.log(sample_input)
// // should return:
// [[1, 0, 9, 9, 9],
//  [0, 9, 9, 9, 0],
//  [1, 0, 9, 0, 0]]

// create your own test cases!

// binary string expansion
// given an input like "1?0?", return an array of all possible outputs you can
// create by replacing the characters "?" with either "0" or "1"
// in the example "1?0?", our output would be something like
// ["1101", "1100", "1001", "1000"]
// (the order may be different depending on how you write the function)
// this algorithm probably needs at least one or two other parameters to
// function properly - there's a few different ways of imagining it
// remember some of the things we've talked about, like passing data between
// function calls, and using default parameters

// function binaryStringExpansion(input, output = []) {

//     return output;
// }

// console.log(binaryStringExpansion("1?0?")) // should contain 4 items
// console.log(binaryStringExpansion("?1?0?")) // should contain 6 items
// console.log(binaryStringExpansion("????")) // should contain 8 items

//////////////////////////////////////////////////////////
// binarySearch(input, target ... ?)
// two parameters - an array of sorted integers to search through (input)
// and an integer to search for (target)
// return true if the target integer is found in the array and false otherwise
// we may define more parameters if necessary
// we gotta do this recursively!
// this will have a big O time complexity of log n
// https://www.bigocheatsheet.com/
count = 0
function binarySearch(input, target) {
    var p = Math.round(input.length/2)
    console.log(input[p])
    if (input[p] == target){
        return true;
    }
    if(input[p] > target){
        return binarySearch(input[p-1], target);
    }
    if(input[p]<target){
        return binarySearch(input[p+1], target)
    }
    return false
}

// all these statements should return true
// if you don't like how these are set up, feel free to write your own
// just remember that the input is sorted

var arr = [1, 2, 3, 4, 6, 7, 9, 11, 12]
console.log(binarySearch(arr, 1) == true)
console.log(binarySearch(arr, 2) == true)
console.log(binarySearch(arr, 3) == true)
console.log(binarySearch(arr, 4) == true)
console.log(binarySearch(arr, 6) == true)
console.log(binarySearch(arr, 7) == true)
console.log(binarySearch(arr, 9) == true)
console.log(binarySearch(arr, 11) == true)
console.log(binarySearch(arr, 12) == true)

console.log(binarySearch(arr, 5) == false)
console.log(binarySearch(arr, 8) == false)
console.log(binarySearch(arr, 10) == false)

console.log(binarySearch(arr, -3) == false)
console.log(binarySearch(arr, 21) == false)