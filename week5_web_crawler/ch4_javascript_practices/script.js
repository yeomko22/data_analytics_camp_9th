var addButton = document.getElementById("add-button");
var todoList = document.getElementById("todo-list");
var todoInput = document.getElementById("todo-input");

addButton.addEventListener("click", function () {
    var todoText = todoInput.value;
    if (todoText !== "") {
		// 새 todo item HTML element 만들어주기
    var listItem = document.createElement("li");
    listItem.className = "todo-item";
    listItem.innerHTML = todoText;

		// 기존 todo list에 추가해주기
    todoList.appendChild(listItem);

		// input 값 비워주기
    todoInput.value = "";
  }
});
