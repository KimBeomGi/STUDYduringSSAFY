<template>
  <div>
    <h2>결정세액 : {{ settledTax }}만원</h2>
  </div>
</template>

<script>
export default {
  name : 'FinaltaxView',
  props : {
    taxBase: Number,                // 과세표준
    reduceTaxData: Number,          // 세액감면액
    TaxAmount: Number,
  },
  data(){
    return{
      // settledTax : ''
    }
  },
  computed:{
    settledTax(){              // 과세표준
      return this.TaxAmount - this.reduceTaxData
    }
  },
}
</script>
  
<style>

</style>