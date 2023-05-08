<template>
  <div>
    <input type="text" v-model.trim="todoInput">
    <button @click="onAddBtnClick">+</button>
  </div>
</template>

<script>
export default {
  name : 'TodoForm',
  data(){
    return {
      todoInput : '',
    }
  },
  methods : {
    onAddBtnClick(){
      // 추가 버튼이 눌려짐...
      // input 요소에 입력된 내용을 stroe에 전달해서
      // 새로운 todoList 요소를 생성
      if(this.todoInput){
        this.$store.dispatch('addTodo', this.todoInput),
        this.todoInput = ''
      }else{
        alert('내용을 입.력.하.세.요!')
      }
    },
  }
}
</script>

<style>

</style>