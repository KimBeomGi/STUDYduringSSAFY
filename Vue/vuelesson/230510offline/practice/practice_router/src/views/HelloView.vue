<template>
  <div>
    <h1>Hello!!! {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name : 'HelloView',
  //route 객체에서 ...params에서 url에 포함되어 있는 변수를 받아올 수 있음
  computed:{
    userName(){
      return this.$route.params.userName
    },
  },
  created(){
    console.log('created!!')
  },
  beforeRouteUpdate(to, from, next){
    console.log(to.params.userName),
    console.log(from.name)
    next()
  }
}
</script>

<style>

</style>