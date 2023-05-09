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
      for (let i=0; i<6; i++){  // 총 6번 반복할 것임. 그리고 반복 마다 숫자 하나씩 뽑기
        let drawNum = Math.floor(Math.random()*45)+1
        while(drawNumbers.indexOf(drawNum) !== -1){
          drawNum = Math.floor(Math.random()*45)+1
        }
        drawNumbers.push(drawNum)
      }
      // this.printNums = drawNumbers.sort(function compare(a,b){return a-b;})
      this.printNums = drawNumbers.sort((a,b) => a-b)
    }
  }
}
</script>

<style>

</style>