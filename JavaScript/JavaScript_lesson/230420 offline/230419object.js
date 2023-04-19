//javascript object >> JSOn 로 변경
//JSON >> javascript object 로 변경

const obj = {
    name : '홍길동',
    age : 17,
    gender : 'male'
}
// 문자열화 하기
objStr = JSON.stringify(obj)
console.log(objStr)
// 문자열을 객체로 만들기(==파싱한다!)
jsonStr = '{"name":"김사피", "age":25,"gender":"female"}'
obj2 = JSON.parse(jsonStr)
console.log(obj2)