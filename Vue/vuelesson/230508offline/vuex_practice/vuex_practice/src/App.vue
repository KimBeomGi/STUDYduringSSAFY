<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <MyComponent2/>
  </div>
</template>

<script>
import MyComponent from '@/components/MyComponent'
import MyComponent2 from '@/components/MyComponent2'

export default {
  name: 'App',
  components: {
    MyComponent,
    MyComponent2,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
