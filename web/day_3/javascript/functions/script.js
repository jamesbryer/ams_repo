"use strict";

// this still works because of hoisting allowing the function to be called before it is defined
console.log(sayHello(1, 2, 3));

function sayHello(num1, num2, num3) {
    return num1 + num2 + num3;
};

// this will not work because the function is not defined until after it is called
// console.log(sayHello2(1, 2, 3));

// using a funcion expression
const sayHello2 = function(num1, num2, num3) {
    return num1 + num2 + num3;
}

// this will work because the function is defined before it is called
console.log(sayHello2(1, 2, 3));

// using an arrow function
const sayHello3 = (num1, num2, num3) => { 
    return num1 + num2 + num3;
}

// even shorter!
const sayHello4 = (num1, num2, num3) => num1 + num2 + num3;

const sayHello5 = console.log("Hello!");
const sayHello6 = console.log("Hello!");

// however, this is really hard to read
// this is a lot more readable! it only avoids a few characters, but it is a lot easier to read
const sayHello7 = (num1, num2, num3) => { return num1 + num2 + num3; }


// QA COMMUNITY Q's 
// Q1
const subtract = (num1, num2) => {return num1 - num2};
console.log(subtract(10, 5));


// Q2
const welcome = (name, age, gender) => {
    console.log(`Hello, I am ${name}, I am ${age} years old and of gender ${gender}`);
}
welcome("James", 25, "male");


// Q3
const powerUp = (num1, num2) => { return Math.pow(num1, num2) };
console.log(powerUp(2, 3));