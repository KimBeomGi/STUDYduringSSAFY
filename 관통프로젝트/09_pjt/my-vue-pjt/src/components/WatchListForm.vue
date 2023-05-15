<template>
  <div class="bg-primary rounded-top bg-opacity-25 p-4">
    <h1>보고싶은 영화</h1>
    <input type="text" v-model.trim="content">
    <button class="border border-primary bg-primary rounded bg-opacity-25" @click="addClick">Add</button>
  </div>
</template>

<script>
export default {
  name : 'WatchListForm',
  data(){
    return{
      content : ''

    }
  },
  
  methods : {
    addClick(){
      if(this.content){
        this.$store.dispatch('createWM',this.content)
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