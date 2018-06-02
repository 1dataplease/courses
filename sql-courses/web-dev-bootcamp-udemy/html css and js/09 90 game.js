// create secretNumber
var secretNumber = 4;

//// ask user for their guess
//// var guess = Number(prompt('guess a number: '));
// typeof guess; //they input a str, use a == 
// OR convert their str to num

//// check if guess is right
// if(guess === secretNumber) {
// 	alert('you got it right!');
// }
// // otherwise say higher or say lower
// else if(guess > secretNumber) {
// 	alert('too high, guess again');
// }
// else {
// 	alert('too low, guess again');
// }

// in future versions it repeats



// 91 - define DRY code - dont repeat yourself,
// 10k comments - loop to print them

// while - print nums 1-5
var count=5;
while(count <= 20) {
	console.log('count is: ' + count);
	count+=2; //count++ is count by 1s
}

// loop thru str, print every char seperately
var str = 'hello';
var count = 0;
while(count < str.length){
	console.log(str[count]);
	count++
}


// 093

// ex 1 - whats this do
var num=1;
while(num <= 10){
	console.log(num);
	num += 2;
}
// 1 3 5 7 9
// it looks like it printed 11, but theres an arrow
// console is showing us the value of the last stmt

// ex 2
var num=1;
while(num <= 20) {
	if(num % 4 === 0) {
		console.log(num);
	}
	num++;
}
// 4 8 12 16 20

// ex 3
// num = 100;
// while(num < 150) {
// 	console.log(num+1);
// 	num--;
// }
// 150 149 infinite

// while ps 1
// print all nums b/w -10 and 19
var num = -10
while(num < 20){
	console.log(num)
	num++;
}

// ps2 - print all even b/w 10 and 40
var num = 9
while(num < 41){
	if(num % 2 === 0){
		console.log(num);
	}
	num++;
}

// ps3 - print all odds b/w 300 and 333
var num = 300
while(num < 334){
	if(num % 2 === 1){
		console.log(num);
	}
	num++;
}

// ps4 - print all nums divisble by 5 and 3 b/w 5 and 50
var num = 5
while(num < 51){
	if(num % 3 === 0 && num % 5 === 0){
		console.log(num);
	}
	num++;
}

//// 095 - annoy - always asks if we're there until answer yes yeah
//// first ask user if there yet
// var answer = prompt('are we there yet?');
// while((answer !== 'yes') && (answer !== 'yeah')){
// 	var answer = prompt('are we there yet?');
// }
// alert('yay we made it');

//// method - index of
var str = 'hello world'
str.indexOf('w'); //6
str.indexOf('world'); //6
str.indexOf('waw'); //-1

//// better version of annoy
// var answer = prompt('are we there yet?');
// while((answer.indexOf('yes') === -1) && (answer.indexOf('yeah') === -1)){
// 	var answer = prompt('are we there yet?');
// }
// alert('yay we made it');

//// 096 - for loops
//// for(initialize; condition; step){}
// print nums 0-5
for(var count=0; count<6; count++){
	console.log(count);
}
var count=0;
while(count < 6) { console.log(count); count++;}

// print each char in str w/ for and w/ while
var str = 'hello'
for(var i = 0; i < str.length; i++){
	console.log(str[i]);
}

var count=0;
while(count < str.length) {
	console.log(str[count]);
	count++;
}

//// 097 for loop exercises
// ex 1
for(var i = 0; i<16; i+=8) {
	console.log(i);
} // 0 8

// ex 2
var str="ahceclwlxo";
for(var i=1; i < str.length; i+=2){
	console.log(str[i]);
} // hello



// 098 for loops, same probs as while loops

// ex1 - print nums b/w -10 and 19
for(var x=-10; x<20; x++) {
	console.log(x);
}

// ex2 - print evens b/w 10 and 40
for(var i=10; i<41; i+=2) {
	if(i % 2 === 0) {
	console.log(i);}

// ex3 - print odds b/w 300 and 333
for(var i=300; i<334; i++) {
	if(i%2 === 1){
		console.log(i);
	}
}

// ex4 - print all nums divisible by 5 and 3; b/w 5 and 50
for(var i=5; i<51; i++) {
	if(i%5===0 && i%3 === 0){
	console.log(i);
	}		
}

