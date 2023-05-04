<template>
  <div>
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
</template>

<script>

export default {
  name: 'TodoForm',
  data(){
    return{
      todoTitle: null,
    }
  },
  methods: {
    createTodo(){
      if(this.todoTitle){
        this.$store.dispatch('createTodo', this.todoTitle) // createTodo를 실행하는데this.todoTitle를 담아서

      }
      else{
        alert('할 일을 입력하세요!!!!')
      }
      this.todoTitle = null
    }
  },
}
</script>

<style>

</style>