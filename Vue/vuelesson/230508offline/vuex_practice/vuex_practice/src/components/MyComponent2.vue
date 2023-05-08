<template>
  <div>
    <h1>Component2</h1>
    <!-- store에서 관리하고 있는 데이터를 출력 -->
    <h1>Number : {{ number }}</h1>
    <!-- <h1>Number : {{ $store.state.number }}</h1> -->
    <!-- 버튼을 누르면, store에 있는 number 변경 -->
    <button>-</button>
  </div>
</template>

<script>
export default {
  name : 'MyComponent2',
  computed : {
    number(){
      return this.$store.state.number   //state가 가지고 있는 number 가지고 오셈
    }
  },
  methods : {
    onClick(){
      
    }
  }
}
</script>

<style>

</style>