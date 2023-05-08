<template>
  <div>
    <input type="text" v-model.trim="todoInput">
    <button @click="onAddBtnClick"></button>
  </div>
</template>

<script>
export default {
  name : 'TodoForm',
  data(){
    return{
      todoInput: ""
    }
  },
  methods:{
    onAddBtnClick(){
      if(this.todoInput){
        this.$store.dispatch('addTodo', this.todoInput),
        this.todoInput = ""
      }else{
        alert('내용을 입력하세요')
      }
    }
  }
}
</script>

<style>

</style>