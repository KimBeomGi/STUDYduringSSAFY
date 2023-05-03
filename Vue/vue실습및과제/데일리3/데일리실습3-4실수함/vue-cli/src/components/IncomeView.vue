<template>
  <div>
    <p>
      연봉 입력 (만원):
      <input type="text" v-model='incomeData' @keyup.enter="emitIncome">
    </p>
    <p>
      세액감면액 (만원):
      <input type="text" v-model='reduceWonData' @keyup.enter="emitReduceWon">
    </p>
  </div>
</template>

<script>
export default {
  name :'IncomeView',
  data(){
    return{
    incomeData : '',
    reduceWonData : '',
    }
  },
  methods: {
    emitIncome(){
      this.$emit('income-input',this.incomeData)
    },
    emitReduceWon(){
      this.$emit('reduceWon-input',this.reduceWonData)
    }
  }
}
</script>

<style>

</style>