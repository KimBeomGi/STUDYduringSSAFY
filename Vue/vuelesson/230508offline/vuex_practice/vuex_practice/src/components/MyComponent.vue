<template>
  <div>
    <h1>Component1</h1>
    <!-- store에서 관리하고 있는 데이터를 출력 -->
    <h1>Number : {{ number }}</h1>
    <h2>doubleNumber : {{ doubleOfNumber }}</h2>
    <!-- <h1>Number : {{ $store.state.number }}</h1> -->
    <!-- 버튼을 누르면, store에 있는 number 변경 -->
    <button @click="onClick">+</button>
  </div>
</template>

<script>
export default {
  name : 'MyComponent',
  computed : {
    number(){
      return this.$store.state.number   //state가 가지고 있는 number 가지고 오셈
    },
    doubleOfNumber(){
      return this.$store.getters.doubleOfNumber
    },
  },
  methods : {
    onClick(){
      // this.$store.state.number++
      // 위 처럼 써도 가능은 하지만 이렇게 사용하지 맙시다.
      // state를 변경할 때는 mutation을 이용 합시다.
      // 1. mutation 호출 해봅시다.
      // 첫번째 인자로 호출하려는 함수, 두번째 인자로 payload
      // this.$store.commit('ADD_NUMBER', 2)
      // 2. action 호출하고, action에서 mutation 호출하기
      // action을 호출하기 위해서는 dispatch()메서드를 이용
      this.$store.dispatch('addNumber', 2)  // index.js의 actions에 있는 addNumber 호출함
    }
  }
}
</script>

<style>

</style>