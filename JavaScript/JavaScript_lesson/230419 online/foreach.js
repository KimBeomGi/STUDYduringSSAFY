const colors = ['red', 'blue', 'green']

const prinfFunc = function (color){
    console.log(color)
}

colors.forEach(prinfFunc)

coclors.forEach(function(color, index, array){
    console.log(colors)
    console.log(index)
    console.log(array)
})

Array.forEach(element => {
    return console.log(color)
});

// 1. 일단 사용해보기
const numbers = [1,2,3]

//  함수 정의(표현식)
const doubleFunc = function(number){
    return number * 2
}

// 함수를 다른 함수의 인자로 넣기(콜백 함수)
// const doubleNumbers = numbers.map(doubleFunc)
// console.log(doubleNumbers) // [2,4,6]
const doubleNumbers = numbers.map(function (number){
    return number *2 
})
console.log(doubleNumbers)


// filter
const products = [
    {name:'cucumber', type:'vegetable'}, // product
    {name:'bananan', type:'fruit'},
    {name:'carrot', type:'vegetable'},
    {name:'apple', type:'fruit'}
]

const fruitFilter = function(product) {
    return product.type === 'fruit' // true 애들만 뽑아서 배열로 만들기
}

const fruits = products.filter(fruitFilter)
console.log(fruits)


