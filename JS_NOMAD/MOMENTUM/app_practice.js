
// // let buttonLabel = "OK";
// // let cancelLabel = "아 거 싫소이다.";
// // let age = parseInt(prompt("How old are you?", buttonLabel, cancelLabel));



// // console.log(isNaN(age))

// // // if(isNaN(age)){
// // //     // condition === true
// // //     console.log("Please write a number")
// // //     age = parseInt(prompt("숫자를 입력하라고 멍청아."))
// // // } else if(age<18){
// // //     console.log("으린느무 스끼가 으데 술을!!!!")
// // //     alert("으린느무 스끼가 으데 술을!!!!")
// // // } else if(age>50){
// // //     console.log("술은 적당히가 좋아요!")
// // //     alert("술은 적당히가 좋아요!")
// // // } else{
// // //     console.log("술! 가능!")
// // //     alert("술! 가능!")
// // // }


// // let i = 1
// // while (isNaN(age) || (age < 1 || age > 150)) {
// //     console.log("Please write a number");
// //     if(isNaN(age)){
// //         age = parseInt(prompt(`숫자를 입력하라고 멍청아. 지금 ${i}번째 말하고 있어.`));
// //     }
// //     else if(age < 1 || age > 150){
// //         age = parseInt(prompt(`거 구라치지마시고 다시하쇼. 참고로 ${i}번째 시도중이여`))
// //     }
// //     i ++
// //   }
// // if(!isNaN(age) && i > 1){
// //     alert('드디어 말 대로 해주었군, 잘해주었어!!')
    
// //     if(age <18){
// //         alert("그른데 으린느무새끼가 으데 술을 마실라고 으잉!!")
// //     }else if(age > 50){
// //         alert("술은 가볍게만 드시고 집으로 귀가하시는 게 좋지 않겠습니까")
// //     }else{
// //         alert("술! 가능!")
// //     }
// // }else{
// //     alert('한 번에 해주다니 고마워!!')
// //     if(age <18){
// //         alert("그른데 으린느무새끼가 으데 술을 마실라고 으잉!!")
// //     }else if(age > 50){
// //         alert("술은 가볍게만 드시고 집으로 귀가하시는 게 좋지 않겠습니까")
// //     }else{
// //         alert("술! 가능!")
// //     }
// // }
// // console.log("Thank you your correct");
// // console.log(age)

/////////////////////////////////////////////////////
// const title = document.getElementById("title")
// console.log(title)
// console.dir(title)

// title.innerText = "Got you"

// console.log(title.id)
// console.log(title.className)


// const hellos = document.getElementsByTagName("h1")

// console.log(hellos)
//////////////////////////////////////////////////////////
// const title = document.querySelector(".hello h1")
// const title2 = document.getElementsByClassName("hello")
// const title3 = document.querySelectorAll(".hello");

// console.log(title.innerText)
// console.log(title2)
// console.log(title3[1])

// const div = document.querySelector(".hello")
// div.style.align = "center"
// console.log(div.style.align)

/////////////////////////////////////////////////////////////////
// // const title = document.querySelector(".hello:first-child h1")
// const divs = document.querySelectorAll(".hello")
// const secondDiv = divs[1]
// const h1 = secondDiv.querySelector("h1:nth-child(2)")

// console.log(h1)
// console.dir(h1)

// h1.innerText = "Hello"
// // title.style.color = "gray"


// function handleTitleClick(){
//     const currentColor = h1.style.color
//     let newColor
//     console.log("title was clicked!")
//     console.log(currentColor + "전")
//     if(currentColor === "red"){
//         newColor = "green"    
//     }else{
//         newColor = "red"
//     }
//     h1.style.color = newColor
//     console.log(currentColor + "후")
// }
// function handleTitleHover(){
//     console.log("마우스를 올렸음")
//     if(h1.style.color){
//         h1.style.cssText = "color: red"
//     }else{
//         h1.style.color = "red"
//     }
//     console.log(h1.style.color)
// }
// function handleTitleLeave() {
//     h1.innerText = "Mouse is gone!"
//     console.log("마우스를 땜")
//     h1.style.cssText = "color: blue"
//     console.log(h1.style.color)
// }
// function handleMouseEnter(){
//     h1.innerText = "Mouse is here!"
//     console.log("마우스 여깄음")
// }
// function handleWindowResize() {
//     document.body.style.backgroundColor = "tomato"
// }
// function handleWindowCopy() {
//     alert("복사했다!!!!!!!")
// }
// function handleWindowOffline() {
//     alert("SOS no WIfi")
// }
// function handleWindowOnline() {
//     alert("야쓰 와이파이 연결됨!!!!!!!")
// }

// h1.addEventListener("mouseover", handleTitleHover)
// h1.addEventListener("mouseleave", handleTitleLeave)

// h1.addEventListener("click", handleTitleClick)
// // h1.onclick = handleTitleClick

// h1.addEventListener('mouseenter',handleMouseEnter )

// window.addEventListener("resize", handleWindowResize)
// window.addEventListener("copy", handleWindowCopy)
// window.addEventListener("offline", handleWindowOffline)
// window.addEventListener("online", handleWindowOnline)
/////////////////////////////////////////////////////////////////
const h1 = document.querySelector("div.hello:first-child h1")
function handleTitleClick() {
  // const clickedClass = "clicked"
  // // if(h1.classList.contains(clickedClass)){
  // //   h1.classList.remove(clickedClass)
  // // }else{
  // //   h1.classList.add(clickedClass)
  // // }
  // h1.classList.toggle(clickedClass)
  h1.classList.toggle("clicked")
    
  console.log(h1.className)
}

h1.addEventListener("click", handleTitleClick)