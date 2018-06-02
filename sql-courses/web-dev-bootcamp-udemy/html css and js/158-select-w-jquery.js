// used to select, then change things

// here we select with $
// also use .css to style elements

// jq very similar to querySelectorAll
// input - css style selector
// output - all elements to match

// select all imgs
$('img')

// select all with class class1 (.)
$(".class1")

// select 1 id with bonus (because dont re-use ids) (#)
$("#bonus")

// select all anchor/link tags inside of a list element ( )
$("li a")

// select only h1 - outputs it inside of a list, even if 1
$("h1")

// select all lis
$("li")

// body
$("body")

// get by id adorable
$("#adorable")

// get a a inside of an li thats inside a ul
$("ul li a")

// 6min - method - .css(css property, new value)

// select h1, run css to change border
$("h1").css("border", "1px solid red")

// do it without jQuery
var demo = document.querySelector("h1");
demo.style.border = "1px solid green";

// jquery can do multiple styles in 1 line
// define styles in an object/dict, pass in object/dict
var styles = {
	color: "red",
	background: "pink",
	border: "2px solid purple"
}

// now select h1, turn it to styles
$("h1").css(styles)

// doing same in vanilla would take longer
var demo = document.querySelector("h1");
demo.style.color = "blue"
demo.style.background = "green"
demo.style.color = "1px solid orange"

// style multiple elements at once
// select all h1s, all lis, make them blue
$("li").css("color", "blue")

// dont have to manually loop thru them 
// like we would in vanilla
lis = document.querySelectorAll("li")
for(var i = 0; i < lis.length; i++){
	lis[i].style.color = "green";
}

// works for text too, ez, dont have to do textContent
$("a").css("font-size", "20px");

// select all lis, apply multiple styles
// alpha is opacity/transparency
$("li").css({
	fontSize: "18px",
	border: "3px dashed purple",
	background: "rgba(89, 45, 20, 0.5)"
});


// when select collection, dont have 2 manually loop thru
// dont have to apply individually
// thats why it always returns selection as a list


























