// 1번
// for 의 i를 const로 설정해놓고는 i++를 이용하여 i의 값을 변경시도 했기 떄문
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
// for (const i = 0; i < nums.length; i++) {  # 변경!
for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 2번

console.log('2번 출력 결과')
// for (num in nums) {    # 변경!
for (num of nums) {
  console.log(num, typeof num)
  // 출력 결과
  // 0 string
  // 1 string
  // 2 string
  // 3 string
  // 4 string
  // 5 string
  // 6 string
  // 7 string
}
