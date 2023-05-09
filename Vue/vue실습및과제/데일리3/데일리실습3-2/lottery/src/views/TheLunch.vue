<template>
  <div>
    <h1>로또</h1>
    <button @click="getLottoNum">Get Lucky Numbers</button>
    <h4>{{ printNums }}</h4>
  </div>
</template>

<script>
export default {
  name:'TheLunch',
  data(){
    return {
      printNums:'행운의 당첨 번호는?!'
    }
  },
  methods : {
    getLottoNum(){
      let drawNumbers = []
      for (i=0; i<6; i++){  // 총 6번 반복할 것임. 그리고 반복 마다 숫자 하나씩 뽑기
        drawNum = Math.floor(Math.random()*45)+1
        if(draw){
          
        }
      }
    }
  }
}
// //중복을 제외하고 7회 돌면서 랜덤 숫자 뽑기
// let randomIndexArray = []
// for (i=0; i<7; i++) {
//   randomNum = Math.floor(Math.random() * 24)
//   if (randomIndexArray.indexOf(randomNum) === -1) {
//     randomIndexArray.push(randomNum)
//   }
// }
// console.log(randomIndexArray)
// // [12, 2, 6, 23, 8, 15]
</script>

<style>

</style>


