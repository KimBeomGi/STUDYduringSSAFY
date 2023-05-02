<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <!-- 3. 사용한다. -->
    <MyComponent />
    <MyComponent />
    <MyComponent />
    <HelloWorld msg="Welcom to Your Vue.js App"/>
    <HelloWorld msg="만나서 반가우이"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from '@/components/MyComponent'  //1. 불러온다.

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent,  //2. 등록한다.
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
