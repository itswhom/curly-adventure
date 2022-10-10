let enterButton = document.getElementById("enter"); // enter button
let inputField = document.getElementById("userinput"); // add item text field
let ul = document.querySelector("ul");
let li = document.querySelectorAll("li");
let span = document.querySelectorAll("span");
let deleteButton = document.getElementsByClassName("deleteBtn");

function inputLength() {
	return inputField.value.length;
}
function refreshElements() {
	li = document.querySelectorAll("li");
	deleteButton = document.getElementsByClassName("deleteBtn");
}
function createListElement() {
	var li = document.createElement("li");
	let newBtn = document.createElement("button");
	newBtn.innerHTML = "Delete";
	newBtn.className = "btn delete";
	li.append(newBtn);
	let newSpan = document.createElement("span");
	newSpan.innerHTML = inputField.value;
	li.append(newSpan);
	ul.appendChild(li);
	inputField.value = "";
	refreshElements();
}

function addListAfterClick() {
	if (inputLength() > 0) {
		createListElement();
	}
	refreshElements();
}

function addListAfterKeypress(event) {
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
	refreshElements();
}

function toggleStrikethrough(e, i) {
	span[i].classList.toggle("done");
}

function deleteItem(e, i) {
	console.log("deleted the item");
	li[i].remove();
	refreshElements();
}

enterButton.addEventListener("click", addListAfterClick);
inputField.addEventListener("keypress", addListAfterKeypress);

for (let i = 0, max = deleteButton.length; i < max; i++) {
	deleteButton[i].addEventListener("click", function(e) {
		deleteItem(e, i);
	});
}

for (let i = 0, max = span.length; i < max; i++) {
	span[i].addEventListener("click", function(e) {
		toggleStrikethrough(e, i);
	});
}

