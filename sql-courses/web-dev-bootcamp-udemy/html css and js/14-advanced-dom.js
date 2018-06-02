// 139 - dom events
// code when someone clicks or something, hovering, drag and drop elements, pressing enter key, arrow keys
// make pgs interactive - change colors/text
// how to make games, form validators

// process - select an element, then add an event listener
// listen for a hover/click event on the <h1> / text input /button

// to add a listener, use method addEventListener
// element.addEventListener(type, functionToCall);

// select a/all buttons, assign it to variable
var button = document.querySelector('button');

// add this 'listener' which listens for (user action, then runs this function)
button.addEventListener("click", function() {
	console.log("someone clicked the button!");
}
);

// now instead of printing to console, put msg on the page
var paragraph = document.querySelector("p");
button.addEventListener("click", function() {
	// change all the textContent within a paragraph tag to be this
	paragraph.textContent = "Someone clicked the Button!";
});

// h1 click anywhere across top of screen, show alert
var h1 = document.querySelector("h1");
h1.addEventListener("click", function() {
	alert("you clicked h1");
});

// can have more than 1 listener on an element, after alert turn orange
var h1 = document.querySelector("h1");
h1.addEventListener("click", function() {
	h1.style.background = "blue";
});

// add listener to clicking on the ul parent element ie any of the lis in it
document.querySelector("ul").addEventListener("click", function() {
	console.log("you clicked the ul");
});

// same but a listener for each li
lis = document.querySelectorAll("li");
// for each, change color of li that was clicked on
for(var i=0; i < lis.length; i++) {
	lis[i].addEventListener("click", function() {
	// could type lis[i], but could write this
	// inside of listener, refers to the item that the event happened on
	this.style.color = "pink";
	});
}
// eventually 1 per ul, then detect which clicked on


// dont have to use anon fxn
var button = document.querySelector("button");
var paragraph = document.querySelector("p");
button.addEventListener("click", ChangeText);

function ChangeText() {
	paragraph.textContent = "Someone clicked the button";
}


// 140 - change background color to purple

var button = document.querySelector("button");
var body = document.querySelector("body");
button.addEventListener("click", ChangeBackground);
function ChangeBackground() {
	body.style.background = "purple";
}

// html has script at top but it relies on fact that button is on page
//  for now we can put the script to the end of the body
//  so that we know the buttons/hs/ have loaded
//  can do diff way once jquery

// couldve done it a little easier / fewer lines
var button = document.querySelector("button");
button.addEventListener("click", function() {
	document.body.style.background = 'purple';
});
// could also have returned document.body with
var body2 = document.getElementsByTagName("body");


// now, hpw to click it and making it back to white

// if green, make purple; if purple make white - put that in the listener fxn
var button = document.querySelector("button");
isPurple = false;
button.addEventListener("click", function() {
	if(isPurple) {
		document.body.style.background = 'white';
		isPurple = false;
	}
	else {
		document.body.style.background = 'purple';
		isPurple = true;
	}
});

// // shorter way of doing the above
// // this only gets read/done automatically if comment out above fxns
var button = document.querySelector("button");
isPurple = false;
button.addEventListener("click", function() {
	if(isPurple) {
		document.body.style.background = 'white';
	}
	else {
		document.body.style.background = 'purple';
	}
	// everytime theres a click, it gets set to the opposite: t, then f etc
	isPurple = !isPurple;
});

// // even shorter way - method called toggle
// // define a css class, toggle it on/off
var button = document.querySelector("button");
button.addEventListener("click", function() {
	// activates the class we made, then if clicked 2nd time, undoes it
	document.body.classList.toggle("purple");
});


// 143
// later write code to count all the events; use 5-10
// mouseover and mouseout
// manipulate 1st li



// 144 - count the number of events on mozilla events page
each event is its own tr
can count num of trs, but might be other tables

document.querySelectorAll("table");
1 main, 1 non-standard, 1 xul, 1 add-on, 1 developer - 5
all 5 tables are full of events

document.querySelectorAll("tr");
says 306
each to each event
but need to exclude 1 header per table, so 301

document.querySelectorAll("tr").length

exclude 5 headers
document.querySelectorAll("tr").length -  document.querySelectorAll("th").length
or - table










