<template>
  <div>
    <p>
      연봉 입력 (만원):
      <input type="text" v-model='anIncomeData'>
    </p>
    <p>
      세액감면액 (만원):
      <input type="text" v-model='reduceTaxData'>
    </p>
    <hr>
    <h2>종합소득금액 : {{ anIncomeData }}만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{}}만원</h2>
    <hr>
    <h2>산출세액 : {{}} 만원</h2>
    <h2>세액감면 : (-)  {{ reduceTaxData }}만원</h2>
    <hr>
    <h2>결정세액 : {{}}</h2>
  </div>
</template>

<script>
// import TaxrateView from '@/components/TaxrateView'

export default {
  name : 'IncomeView',
  components:{
    // TaxrateView,
  },
  data(){
    return{
      anIncomeData : '',    // 연봉
      reduceTaxData : '',   // 세액감면액
      taxBase: '',          // 과세표준
    }
  },
}
</script>

<style>

</style>