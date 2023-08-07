"use strict";

// The structure of this page is, in general, the format you should follow when creating a JS script
// Select the elements you need from the page, add the fuctions you need then create the event listeners

//  *** Selectors ***


// document.getElementById() - not used much anymore so avoid using it!
// document.querySelector() - returns the first element that matches a given CSS-style selector
//buttons from page
let btnOne = document.querySelector("#btnOne");
let btnTwo = document.querySelector("#btnTwo");

// inputs from page
let inputOne = document.querySelector("#inputOne");
let inputTwo = document.querySelector("#inputTwo");

// divs from page
let mainDiv = document.querySelector("#mainDiv");



// *** Functionality ***
let add = () => {
    let valueOne = parseInt(inputOne.value);
    let valueTwo = parseInt(inputTwo.value);

    let valueDiv = document.createElement("div");
    let myValue = document.createTextNode(`${valueOne} + ${valueTwo} = ${valueOne + valueTwo}`);

    valueDiv.appendChild(myValue);
    mainDiv.appendChild(valueDiv);

}

let clearResults = () => {
    mainDiv.innerHTML = "";
}


// *** Event Listeners ***
addBtn.addEventListener("click", clearResults);
addBtn.addEventListener("click", add);
clearBtn.addEventListener("click", clearResults);