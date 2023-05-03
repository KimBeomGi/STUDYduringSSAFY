<template>
  <div>
    <p>
      연봉 입력 (만원):
      <input type="number" v-model='anIncomeData'>
    </p>
    <p>
      세액감면액 (만원):
      <!-- <input type="number" v-model='reduceTaxData'> -->
      <input type="number" v-bind:value="reduceTaxData" v-on:input="reduceTaxData = parseInt($event.target.value)" />
    </p>
    <hr>
    <h2>종합소득금액 : {{ anIncomeData }}만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{ taxBase }}만원</h2>
    <hr>
    <TaxrateView v-bind:reduce-tax-data='reduceTaxData' v-bind:tax-base='taxBase'/>
    <hr>
    <!-- <FinaltaxView/> -->
  </div>
</template>

<script>
import TaxrateView from '@/components/TaxrateView'
// import FinaltaxView from '@/components/FinaltaxView'

export default {
  name : 'IncomeView',
  components:{
    TaxrateView,
    // FinaltaxView,
  },
  data(){
    return{
      anIncomeData : 0,    // 연봉
      reduceTaxData : 0,   // 세액감면액
    }
  },
  computed:{
    taxBase(){              // 과세표준
      if(this.anIncomeData - 150 < 0){
        return 0
      }
      else{
        return this.anIncomeData - 150
      }
      
    }
  },
}
</script>

<style>

</style>