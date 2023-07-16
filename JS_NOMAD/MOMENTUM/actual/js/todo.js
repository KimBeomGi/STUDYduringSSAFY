const toDoForm = document.getElementById("todo-form")
const toDoInput = document.querySelector("#todo-form input")
// const toDoInput = toDOForm.querySelector("input")
const toDoList = document.getElementById("todo-list")

const TODOS_KEY = "todos"

let toDos = []

function saveToDos() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos))
}

function deleteTodo(event) {
  const li = event.target.parentElement
  // console.log(li.id)
  li.remove()
  // console.log(typeof li.id)
  toDos = toDos.filter(toDo => toDo.id != parseInt(li.id))    // localstorage에서 지우기 위한 기능
  saveToDos()
}


function paintTodo(newTodo) {
  console.log("i will paint", newTodo)
  const li = document.createElement("li")
  li.id = newTodo.id
  const span = document.createElement("span")
  span.innerText = newTodo.text
  const button = document.createElement("button")
  button.innerText = "❌"
  button.addEventListener("click",deleteTodo)
  li.appendChild(span)
  li.appendChild(button)
  toDoList.appendChild(li)
}

function handleTodoSubmit(event) {
  event.preventDefault()
  // console.log(toDoInput.value)
  const newTodo = toDoInput.value //여기서 newTodo로 이미 복사가 되었기에 이후에 toDoInput.value로 뭘 해도 newTodo에 영향X
  toDoInput.value = ""
  const newTodoObj = {
    text:newTodo,
    id: Date.now()
  }
  toDos.push(newTodoObj)
  paintTodo(newTodoObj)
  saveToDos()
}

toDoForm.addEventListener("submit", handleTodoSubmit)

// function sayHello(item){
//   console.log("this is the turn of", item)
// }


const savedToDOs = localStorage.getItem(TODOS_KEY)

console.log(savedToDOs)
if(savedToDOs !== null){
  const parsedToDos = JSON.parse(savedToDOs)
  toDos = parsedToDos
  // console.log(parsedToDos)
  // parsedToDos.forEach((item) => console.log("this is turn of ", item))
  parsedToDos.forEach(paintTodo)
}