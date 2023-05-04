<template>
  <div>
    <h2>산출세액 : {{ taxAmount }} 만원</h2>
    <h2>세액감면 : (-)  {{ reduceTaxData }}만원</h2>
    <hr>
    <FinaltaxView 
      v-bind:tax-base='taxBase' 
      v-bind:reduce-tax-data='reduceTaxData'
      v-bind:tax-amount='taxAmount'
      />
  </div>
</template>

<script>
import FinaltaxView from '@/components/FinaltaxView'
export default {
  name : 'TaxrateView',
  props : {
    taxBase: Number,                      // 과세표준
    reduceTaxData: Number,                // 세액감면액
  },
  components :{
    FinaltaxView,
  },
  data(){
    return{
      taxAmount: '',                       // 산출세액
    }
  },
  methods:{
    calculateTaxAmount(){                 // 산출 세액 결정함수
      if(this.taxBase>100000){            // 과세표준이 10억원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.45 - 6540)
      }
      else if(this.taxBase>50000){        // 과세표준이 5억원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.42 - 3540)
      }
      else if(this.taxBase>30000){        // 과세표준이 3억원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.40 - 2540)
      }
      else if(this.taxBase>15000){        // 과세표준이 1.5억원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.38 - 1940)
      }
      else if(this.taxBase>8800){         // 과세표준이 8800만원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.35 - 1490)
      }
      else if(this.taxBase>4600){         // 과세표준이 4600만원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.24 - 522)
      }
      else if(this.taxBase>1200){         // 과세표준이 1200만원 초과시
        this.taxAmount = Math.round(this.taxBase * 0.15 - 108)
      }
      else{
        this.taxAmount = Math.round(this.taxBase * 0.06)
      }
    }
  },
  watch: {
    taxBase(){
      this.calculateTaxAmount()
    }
  },
  computed :{

  },
  created(){
    console.log('객체 생성됨!')
    this.calculateTaxAmount()
  },
}
</script>

<style>

</style>