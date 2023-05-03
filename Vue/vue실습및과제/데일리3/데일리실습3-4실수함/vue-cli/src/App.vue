<template>
  <div id="app">
    <h1>소득세 계산기</h1>
    <IncomeView @income-input="handleIncomeInput" @reduceWon-input="handleReduceWonInput"/>
    <hr>
    <h2>종합소득금액: {{ incomeData }} 만원</h2>
    <h2>종합소득공제: (-) 150 만원</h2>
    <h2>과세표준: {{}} 만원</h2>
    <hr>
    <h2>산출세액: {{}} 만원</h2>
    <h2>세액감면: (-) {{ reduceWonData }} 만원</h2>
    <hr>
    <h2>결정세액: {{}} 만원</h2>

  </div>
</template>

<script>
import IncomeView from '@/components/IncomeView'

export default {
  name: 'App',
  components: {
    IncomeView,
  },
  data(){
    return{
      incomeData:'',
      reduceWonData:'',
    }
    
  },
  methods:{
    handleIncomeInput(incomeData){
      this.incomeData = incomeData
    },
    handleReduceWonInput(reduceWonData){
      this.reduceWonData = reduceWonData
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
