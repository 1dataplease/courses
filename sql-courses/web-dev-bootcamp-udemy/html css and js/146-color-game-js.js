// responsive, change header after correct
// change all 6 after correct

// if one you clicked is wrong, it disappears, it says try again
// if right, change all remaining boxes to correct color

// 147
// 1 - add 6 squares
// each is a div w class=square
// always have a tester
// alert('connected');

// set up squares to make each a diff color
// without randomized, assign 6 colors always the same
// list
var colors = [
'rgb(255,0,0)',
// yellow
'rgb(255,255,0)',
'rgb(0,255,0)',
// teal / cyan
'rgb(0,255,255)',
'rgb(0,0,255)',
// light purple
'rgb(255,0,255)',
]

// then select all 6 squares, loop thru them. assign 1 to each
// grab 6 squares
var squares = document.querySelectorAll(".square");

// every time pg loads, 1 of the colors is selected to be the goal
// start w hard code, then randomize
// has to be above the 4loop
var pickedColor = colors[3];

// for now, will replace RGB with name of correct color
// using span in place of rgb
// assign colorText var to that span, so we can assign text to it
var colorText = document.getElementById("colorText");

// update colorText so it says pickedColor
colorText.textContent = pickedColor;

for(var i=0; i < squares.length; i++){
	// adds initial colors to squares
	// squares[0] background = 0th color
	squares[i].style.background = colors[i];
	
	// add clickListeners for each square
	squares[i].addEventListener("click", function(){
		// grab color of clicked square
		// alert(this.style.background);
		var clickedColor = this.style.background;

		// no idea why this isnt working!!!! only wrongs
		// compare color to pickedColor
		// clickedColor not working
		if(clickedColor === pickedColor){
			alert("Correct");
		} else {
			this.style.background = "#232323";
		}
	});
}

// will generate 3 different numbers from 0-255






// add logic for click events
// when click on square
// figure out color of clicked square
// compare that color to the pickedColor/winningColor
// if different, change backgroundColor of square to background
// if same, player wins

// add clickHandler that alerts for each square into square loop



