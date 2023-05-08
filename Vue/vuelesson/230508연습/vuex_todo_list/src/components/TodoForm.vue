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
    return{
      todoInput: '',
    }
  },
  methods:{
    onAddBtnClick(){
      if(this.todoInput){ //todoInput이 값이 존재하면! trim을 통해 다 지웠으니까
        this.$store.dispatch('addTodo', this.todoInput),    // actions의 addTodo 함수를 실행
        this.todoInput = ''
      }else{
        alert('내용을 입력하세요')
      }
    },
  },
}
</script>

<style>

</style>