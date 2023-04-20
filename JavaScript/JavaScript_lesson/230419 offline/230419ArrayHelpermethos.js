const arr = [6,2,7,3,1,9,4,20,100, 101]
//map(함수, iterable):배열의 모든 요소에 대해서 함수실행해서 그 결과를 모아서 새로운 배열을 생성
// let new_arr = []
// for (el of arr):{
//     new_arr.push(el-50)
// }
// console.log(new_arr)
let new_arr = arr.map(x=>x-50)
console.log(new_arr)
//filter : 인자로 받은 함수가 true를 반환하면 해당하는 요소를 포함하는 새로운 배열을 만들어냄.
// 짝수만 모아서 새로운 배열을 만드려
// function isEven(x){
//     return x%2==0
// }
// new_arr = arr.filter(isEven)
// new_arr = arr.filter(x=>x%2==0)
// console.log(new_arr)

let result = arr.find(x=>x%2!==0)
console.log(result)
//some: 모든 요소에 대해서 콜백함수가 하나라도 참을 반환하면 True
result = arr.some(x=> x > 100)
console.log(result)
//every: 모든 요소의 콜백함수가 참을 반환하면 True
result = arr.every(x=> x < 200)
console.log(result)