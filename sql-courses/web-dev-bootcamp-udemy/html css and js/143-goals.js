// 3 min - manipulate 1st li
// 1st make variable for the 1st of several lis
var firstLI = document.querySelector("li");

// // 2nd make evetlistener, add what it does
// // tested console, then turn green, want a toggle
// // do 2 diff listeners instead
// firstLI.addEventListener("mouseover", function() {
// 	// console.log('test works');
// 	firstLI.style.color = "green";
// });

// firstLI.addEventListener("mouseout", function() {
// 	firstLI.style.color = "black";
// });

// now do it for all 3 lis instead of just 1st one
var lis = document.querySelectorAll("li");


// cant just do lis.addEvent
// have to do a forEach or something
// also, didnt work when i said lis[i], had to say this
for(var i = 0; i < lis.length; i++){
	// lis[i].addEventListener("mouseover", function() {
	// 	this.style.color = "green";
	// });
	// lis[i].addEventListener("mouseout", function() {
	// 	this.style.color = "black";
	// });

	// this clicks and strikes thru
	lis[i].addEventListener("click", function() {
		this.classList.toggle("done");
	});

	// this adds a class
	lis[i].addEventListener("mouseover", function() {
		this.classList.add("selected");
	});

	// this removes that class
	lis[i].addEventListener("mouseout", function() {
		this.classList.remove("selected");
	});
	

}

// added class done, done can be like 