<template>
  <div id="app">
    <div class="d-flex justify-content-end blue justify-content-md-between" >
      <img class="img-fluid" src="./assets/ssafy_logo.png" alt="">
      <nav class="d-flex justify-content-md-around"> 
        <router-link class = "text-decoration-none" :to="{name : 'movies'}">Movies</router-link> 
        <router-link class = "text-decoration-none" :to="{name : 'random'}">Random</router-link> 
        <router-link class = "text-decoration-none" :to="{name : 'watchlist'}">Watch list</router-link> 
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name : 'App',
  data(){
    return{

    }
  },
  methods:{

  },
  created(){
    this.$store.dispatch('getCards')
  }
}
</script>

<style>

*{
  font-family: 'Single Day', cursive;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 4rem
}

nav a.router-link-exact-active {
  color: #42b983;
  
}

.blue{
  background-color: #BBDEFB;
}

img {
  width: 5%;
}



</style>
