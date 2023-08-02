// The following are the different types of console messages
console.log("Hello World! This is console.log()")
console.warn("This is a warning!")
console.error("This is an error!")
console.info("This is an info!")

// Variables
// var, let, const
// var is globally scoped
// let is block scoped
// const is block scoped and cannot be reassigned

var myNumber = 100;
const myConstantNumber = 200;

//reassignment
myNumber = 200;

//myConstantNumber = 300; // This will throw an error

console.log("This is a %c message with some %c styling", "color: red; font-size: 20px;", "color: blue; font-size: 30px;")

stringOne = "Hello"; 
stringTwo = "World";

// template literals

console.log(`This is a string literal ${stringOne} ${stringTwo}`);

console.log(`The sum of 5 + 5 is ${5 + 5}`);

// QA Community task
console.log("James");
console.log("Bryer");
console.log("Sussex");
console.log("Gemini");

let make = "Lotus";
let model = "Emira";

console.log(`My favourite car is a ${make} ${model}`);

console.log("%c Hello, World!", "font-size: 25px; color: orange; font-family: fantasy; font-weight: bold; background-color: black; padding: 10px; border-radius: 10px;")

// this just says undefined - it doesn't throw an error. DON'T DO THIS
console.log(x);
var x = 10;

// this throws an error - USE THIS 
console.log(y);
let y = 10;

// this works because var is globally scoped - DON'T DO THIS
aeg = 10;

// do NOT use implicit global variables

// we should use script mode to throw errors for undeclared variables
"use strict";