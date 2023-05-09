<template>
  <div id="app">
    <main id="">
      <SideBar/>
      <div>
        <router-view/>
      </div>
    </main>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  name : 'App',
  components : {
    SideBar,
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
}

main{
  padding: 5px;
}

</style>
