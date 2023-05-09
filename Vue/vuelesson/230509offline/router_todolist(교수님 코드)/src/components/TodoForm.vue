<template>
  <div>
    <button @click="addClick">+</button>
    <input type="text" v-model.trim="content">
  </div>
</template>

<script>
export default {
  name : 'TodoForm',
  data(){
    return {
      content : ''
    }
  },
  methods : {
    addClick(){
      if(this.content){
        this.$store.dispatch('createTodo',this.content)
        this.content = ''
      }else{
        alert('내용을 입력하세요')
      }
    }
  }
}
</script>

<style>

</style>