// // // 함수 선언하기
// // function myFunc(){  // 선언식 실행전에 메모리에 로딩함!!
// //     console.log('myFunc call')
// // }
// // // 표현식(Expression): 익명함수(함수에 이름이 없으므로)를 변수에 담아 쓰기
// // const myFunc2 = function(){
// //     console.log('myFunc2 call')
// // }

// // myFunc() // 함수 호출
// // myFunc2()


// // 함수 선언하기
// // function myFunc(){  // 선언식 실행전에 메모리에 로딩함!!
// //     console.log('myFunc call')
// // }
// // 표현식(Expression): 익명함수(함수에 이름이 없으므로)를 변수에 담아 쓰기
// const myFunc2 = function(num1, num2, ...args){// 개수가 정해져있지않은 args를 받겠음.
//     // console.log('myFunc2 call')
//     console.log(arguments)
//     console.log(args)
//     // for(let i=0; i< arguments.length; i++){

//     // }
    
//     let result = 0
//     for( arg of arguments){ // 다 더하기!
//         result += arg
//     }
//     return result
// }

// // myFunc() // 함수 호출
// let result = myFunc2(1,2,3,4,5,6,7,8,9,10)
// console.log(result)


// let arrow = x => {
//     console.log(x)
//     return x*x
// }
// result = arrow(10)
// console.log(result)


// key = lambda x : x[0]
// key = x => x[0]
// let arrow = x => x => x*x
// result = arrow(10)
// console.log(result)


//javascript에서의 함수는 일종의 객체 : 인자로도 전달되고, 변수에도 넣을수 있고: 다 됨
function funcA(){
    console.log('Function A호출!!')
    return function(){
        console.log('반환 함수 호출!!')
    }
}
// let returnFunction = funcA()
// returnFunction()
// funcA()()
(function(){
    console.log('이건 어떻게 실행하나요?')
})()