const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    var quater = 25
    var dime = 10
    var nickle = 5
    var pennys = 1
    var coinbag = {}
    var count = 0
    while (cents> quater){
        count += quater
        console.log(count)
    }
    count -= quater
    if (cents%count == 0){
        coinbag.push({quater: count/quater})
    }
    // else{

    // }
    return 
}