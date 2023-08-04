"use strict";

// Objects in JavaScript

// Object literal notation
var person = {
    name: "John",
    age: 32,
    isMarried: false,
    children: ["Anna", "Peter"],
    sayHello: function() {
        console.log("Hello!");
    }
};

console.log(person.name);
//console.log(person);
// Notice the order of the properties is not preserved
console.info(person);

let James = new Object();
James.name = "James";
James.age = 25;
James.isMarried = false;
James.children = [];
James.sayHello = function() {
    console.log("Hello!");
};

// these two are equivalent but the first one is preferred for readability 
// however, the second one is useful when the property name is a variable
console.log(James.name);
console.log(James["name"]);


let darthVader = {
    allegiance: "Empire",
    weapon: "lightsaber",
    sith: true
};

if (darthVader.sith) {
    darthVader.jedi = false;
};

console.log(darthVader.allegiance);
console.log(`Darth Vader is jedi: ${(darthVader.allegiance == "Jedi")? "Yes" : "No"}`);
console.log(`Darth Vader is jedi: ${(darthVader.jedi)? "Yes" : "No"}`);

let myArray = ["hello", "everyone"];

myArray.push("my");
myArray.push("name");
myArray.push("is");
myArray.push("James");

console.log(myArray.length);

// removing an element from the end of the array using shift - removes the first element and returns it

myArray.shift();
console.log(myArray.length);

// for of loop to iterate over the array returning the values not the keys
for (let value of myArray){
    console.log(value);
};

