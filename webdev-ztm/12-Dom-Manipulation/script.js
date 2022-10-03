var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var todoItem = document.getElementsByClassName("item");
function inputLength() {
    return input.value.length;
}

function createListElement() {
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(input.value))
    li.classList.add("item");
    ul.appendChild(li);
    input.value = "";
}

function toggleDone() {
    this.classList.toggle("done");
}

function addListAfterClick() {
    if(inputLength() > 0) {
    var li = document.createElement("li");
        createListElement();
    }
}

function addListAfterKeypress(event) {
    if(inputLength() > 0 && event.key === 'Enter') {
        createListElement();
    }
}

button.addEventListener("click", addListAfterClick);
todoItem.addEventListener("click", toggleDone);
input.addEventListener("keypress", addListAfterKeypress);

