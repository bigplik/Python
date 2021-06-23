

const log0 = document.getElementById('values0');
//const log = document.getElementById('values');
//const log2 = document.getElementById('values2');
var button = document.getElementById('clear');


//generate random whole numbers within a range
/*
//1st
function ourRandomRange(ourMin, ourMax) {

    return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
}
console.log(ourRandomRange(1, 9))//
*/
let numbers = 0;
let numbersArray = [];
//2nd
function randomRange(myMin, myMax) {
    var i = 0;
    while (i < 6) {
        numbersArray.push(Math.floor(Math.random() * (myMax - myMin + 1)) + myMin);
        i++;
    }
    //numbers = Math.floor(Math.random() * (myMax - myMin + 1)) + myMin;

    return log0.textContent = `${numbersArray[0]} ${numbersArray[1]}
    ${numbersArray[2]} ${numbersArray[3]} ${numbersArray[4]} ${numbersArray[5]}`;
}


//var myNumbers = randomRange(1,49);

button.addEventListener('click', (e) => {
        e.preventDefault();
        randomRange(1,49);
        numbersArray = [];
});

/*
form.addEventListener('submit', (e) => {
    e.preventDefault();
    todoMaker(input.value);
    input.value = "";//by this we will clear out input value for next time
});

// Step 3 -> create a todoMaker function that creates 'li' elements with the text user provides
// from their form and appends it to the 'ul'.
var todoMaker = (text) => {
    var todo = document.createElement('li');
    todo.textContent = text;
    todosList.appendChild(todo);
}
*/


//usuwanie podpowiedzi z okna wyboru
//Wpisujemy pierwsze litery witryny, którą chcemy usunąć z przeglądarki. 
//Następnie za pomocą klawiszy strzałek podświetlamy pozycję do usunięcia.
//W przypadku macOS jest to kombinacja Shift + fn + Delete.