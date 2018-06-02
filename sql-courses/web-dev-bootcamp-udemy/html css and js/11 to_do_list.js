console.log('connected');

// auto 1st goal
var goals = ['buy a turtle'];

// fxns to be used before so more readable
function listGoals(){
	goals.forEach(function(goal, i){
			// goals.indexOf(goal)

			console.log('*******');
			console.log(i + ': ' + goal);

		});
		console.log('*******');
	}

function addGoal(){
	var newGoal = prompt('Enter new goal: ');
	// add it to the goals Array
	goals.push(newGoal);
	// feedback letting user know it worked
	console.log('added goal');
}

function deleteGoal(){
	// ask for the goal index
	var index = prompt('Enter goal index you want to delete: ');
	// delete from array - not pop or shift
	goals.splice(index, 1);
	console.log('deleted goal');
}

// ask user for input
var input = prompt('enter new, list, delete or quit')

while(input !== 'quit') {
	
	if(input === 'list') {
		listGoals();
	}
	
	else if(input === 'new') {
		addGoal();
	}
	
	else if(input === 'delete') {
		deleteGoal();
	}

	// one they finish their list or new, ask them again
	input = prompt('enter new, list, delete or quit');
}

console.log('ok you quit the app');

// new adds item to array, gives it a number

// list prints the array *** goal1, goal2, ... ****
