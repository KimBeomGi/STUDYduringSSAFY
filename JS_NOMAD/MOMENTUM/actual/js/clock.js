const clock = document.querySelector("#clock")

// function getClock() {
//   const date = new Date()
//   if(date.getSeconds() < 10){
//     const dateSeconds = "0"+date.getSeconds()
//     clock.innerText = `${date.getHours()}:${date.getMinutes()}:${dateSeconds}`
//   } else{
//     clock.innerText = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
//   }
// }
function getClock() {
  const date = new Date()
  const hours = String(date.getHours()).padStart(2,"0")
  const minutes = String(date.getMinutes()).padStart(2,"0")
  const seconds = String(date.getSeconds()).padStart(2,"0")
  clock.innerText = `${hours}:${minutes}:${seconds}`
  
}


// setInterval(sayHello, 5000) // 이건 주기적으로 출력

// setTimeout(sayHello, 5000) // 이건 한번만 출력

getClock()
setInterval(getClock, 1000)