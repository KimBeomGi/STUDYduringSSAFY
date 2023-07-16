const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")

const link = document.querySelector("a")
const greeting = document.querySelector("#greeting")
const HIDDEN_CLASSNAME = "hidden"
const USERNAME_KEY = "username"

function onLoginSubmit(event) {
  event.preventDefault()
  // const username = loginInput.value
  //  console.log(username)
  console.log(event)
  loginForm.classList.add(HIDDEN_CLASSNAME)
  const username = loginInput.value
  localStorage.setItem(USERNAME_KEY, username)
  paintGreetings(username)
  console.log(username)
}

function paintGreetings(username) {
  // const username = localStorage.getItem(USERNAME_KEY)
  greeting.innerText = `Hello ${username}`
  greeting.classList.remove(HIDDEN_CLASSNAME)
}

// loginForm.addEventListener("submit", onLoginSubmit)

const savedUsername = localStorage.getItem(USERNAME_KEY)

console.log(savedUsername)

if(savedUsername === null){
  //show the form
  loginForm.classList.remove(HIDDEN_CLASSNAME)
  loginForm.addEventListener("submit", onLoginSubmit)
} else{
  //show the greetings
  paintGreetings(savedUsername)

}