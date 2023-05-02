<template>
  <div>
    <h1>MyComponent</h1>
    <p> {{msg}}</p>
  </div>
</template>

<script>

export default {
  name : 'MyComponent',
  data(){
    return{
    msg: '안녕하세요'
    }
  }
}
</script>

<style>

</style>