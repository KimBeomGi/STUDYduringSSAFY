// 문제풀이
// 1. 첫 줄부터 총 1,3,5,7,9 개의 별이 있다.
// 2. 띄어쓰기는 4,3,2,1,0의 띄어쓰기가 있다.
// 3. 반복문을 이용하자.
// let star = '*'
// let space = '    '
// for (let i = 0; i < 5; i++) {
//     console.log(star)
//     space -= ' '
//     star += '**'
// }
let space = ' '
let star = '*'
for (let i = 0; i < 5 ; i++) {
    console.log(space.repeat(4-i) + star.repeat((2*(i+1)-1)))
}

// let test = '123';
// testRepeat = test.repeat(3);
// console.log(testRepeat)