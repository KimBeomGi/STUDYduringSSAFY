// 매개변수보다 인자의 개수가 적을 경우(매개변수와 인자의 불일치 허용)
const threeArgs = function(arg1, arg2, arg3){
    return [arg1, arg2, arg3]
}

threeArgs()

// Spread syntax (Rest parameters)
const restArgs = function(arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
}

restArgs[1,2,3,4,5]

// Arrow function
const arrow1 = function(name){
    return `hello ${name}`
}

// 1. function 키워드 생략 가능
const arrow2 = (name) =>{
    return `hello ${name}`
}

// 2. 인자가 1개인 경우에만 {} 생략 가능
const arrow3 = name =>{
    return `hello ${name}`
}

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & retrun 삭제 가능
const arrow4 = name => `hello ${name}`


const myFunc = function(){
    console.log(this)
}
myFunc()


const myObj ={
    numbers : [1,2],
    myFunc() {
        console.log(this) //myObj
        this.numbers.forEach(function (number){
            console.log(number) // 1
            console.log(this) // window
        })
    }
}

//화살표 함수 이용
const myObj = {
    numbers: [1,2]
    myFunc() {
        console.log(this) // myObj
        this.numbers.forEach((number) => {
            console.log(number) //1
            console.log(this) //myObj
        })
    }
}


const key = 'country'
const value = ['한국', '일본', '중국']

const myOBj = {
    [key] : value,
}
console.log(myObj)
console.log(myObj.country)




const userInformation = {
    name: '손임현',
    userId: 'ssafygood',
    email: 'ssafy@ssafy.com',
}

const name = userInformation.name
const userId = userInformation.userId

console.log(name)
console.log(userId)

// 아래처럼 가능!
const userInformation = {
    name: '손임현',
    userId: 'ssafygood',
    email: 'ssafy@ssafy.com',
}

const {name, userId} = userInformation
console.log(name, userId)