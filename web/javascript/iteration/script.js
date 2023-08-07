// for (let i = 0; i < 10; i++) {
//     console.log(i);
// }

// let count = 1;
// let flag = true;
// while (flag) {
//     console.log(count);
//     count++;
//     if (count > 10) {
//         flag = false;
//     }
// }

// let count2 = 1;
// let flag2 = true;
// do {
//     console.log("Flag 2 isn't true! I'm running anyway! Next iteration...");
//     count2++;
// } while (!flag2);

"use strict";

// for (let A = 100; A <= 200; A++){
//     console.log(`A = ${A}`);
// }

// for (let A = 100; A <= 200; A++){
//     if (A%2==0){
//         console.log("-");
//     }else{
//         console.log("*");
//     }
// }

for (let i = 1; i <= 10; i++) {
    for (let j = 1; j <= 10; j++){
        console.log(j);
    }
}

// USE F2 TO RENAME VARIABLES FROM THE FIRST INSTANCE OF THE VARIABLE NAME

// ternary operator
// condition ? true : false;
let numA = 10;
let numB = 20;
// brackets are evaluated like an if statement, then the first value is returned if true, the second if false
let myNumber = (numA > numB)? 10 : 20;


// 1
let strictA = true;
let strictB = 1;

console.log(strictA == strictB);
console.log(strictA === strictB);



//  2
console.log(strictA != strictB);
console.log(strictA !== strictB);



//  3
let age = 66;
if (age > 18 && age < 65) {
    console.log("Age is in range");
}else {
    console.log("Age is not in range");
}



//  4
let rslt = (age >= 50) ? "50 or over" : "Under 50";
console.log(`Age: ${rslt}`);



//  5
let date = new Date();
let today = date.getDay();

switch (today) {
    case 0:
        console.log("It is Sunday");
        break;
    case 1:
        console.log("It is Monday");
        break;
    case 2:
        console.log("It is Tuesday");
        break;
    case 3:
        console.log("It is Wednesday");
        break;
    case 4:
        console.log("It is Thursday");
        break;
    case 5:
        console.log("It is Friday");
        break;
    case 6:
        console.log("It is Saturday");
        break;

}