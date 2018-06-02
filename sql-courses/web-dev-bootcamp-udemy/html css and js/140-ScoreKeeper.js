// 140 - 430

//  // test at first as usual
// alert('connected');

// have vars that are pointers to all 3 buttons
// when pointing to a id (not class), have to put a #
var p1Button = document.querySelector("#p1");
var p2Button = document.querySelector("#p2");
var resetButton = document.getElementById("reset");

// // now make all of them listen
// // when click p1, add 1 to p1score, same with p2, change text
var p1score = 0;
var p2score = 0;

// set this as max, adjustable
var maxScore = 5;
// create variable where game is over t/f, update it
var gameOver = false;
// put logic if p1/2score >= maxScore, gameOver=True
// if gameover=True, do not add
// all this goes in the event handler so it knows not to add

var p1display = document.querySelector('#p1Display');
var p2display = document.querySelector('#p2Display');

// slider variable
var numInput = document.querySelector("input");

// the span inside a paragraph that changes the maxScore
var maxScoreDisplay = document.querySelector("p span");

// // create function that updates score
// // for some reason this really makes p2 button slow/not work
// function updateP1Score() {
// 	// p1score = p1score + 1;
// 	p1score ++;
// 	p1display.textContent = p1score;
// }

// function updateP2Score() {
// 	// p2score = p2score + 1;
// 	p2score ++;
// 	p2display.textContent = p1score;
// }

// add to 0 to 0 when one is clicked
// p1Button.addEventListener("click", updateP1Score);
// p2Button.addEventListener("click", updateP2Score);

// could make these thinner, but ok
// making fxns anon instead of referall speeded it up
p1Button.addEventListener("click", function() {
	if(!gameOver) {
		p1score ++;
		p1display.textContent = p1score;
		// will keep going until 
		if(p1score >= maxScore) {
			gameOver = true;
			p1Display.style.color = "green";
		}
	}
});

p2Button.addEventListener("click", function() {
	if(!gameOver) {
		p2score ++;
		p2display.textContent = p2score;
		// have to do a 2nd check after this, change to over
		if(p2score >= maxScore) {
			gameOver = true;
			// p2Display.classList.add("winner");
			p2Display.style.color = "green";
		}
	}
});


// 142

function reset() {
		p1score = 0;
		p2score = 0;
		gameOver = false;
		p1display.textContent = p1score;
		p2display.textContent = p2score;
		// p1Display.classList.remove("winner");
		p1display.style.color = "black";
		p2display.style.color = "black";
};

// now that it stops at 5, make the reset button set scores 0
resetButton.addEventListener("click", function() {
	reset();	
});


// make display green once score to 5 - insert in line 53, 64

// now, need slider to change maxScore
// add an event, when input changes, the maxScore does
numInput.addEventListener("change", function() {
	// this takes the 5, changes it to the value in the box
	// maxScoreDisplay.textContent = this.value;
	maxScoreDisplay.textContent = numInput.value;
	// now need to change maxScore to the new num
	
	// couldve set above to == so it would know 1 = "1"
	// maxScore = Number(this.value);
	maxScore = Number(numInput.value);

	// also want the game to reset, take many lines
	reset();
});

//  tried to set this at top so buttons can know the maxScore
//  but then resetButton didnt work
// comparing p1/p2 score num to the maxScore which we turned str

// if want to change maxScore
// could reset all to 0
// continuing to play
// better - reset to 0 whenever we change maxScore
// see reset fxn and input it into numInput listener

