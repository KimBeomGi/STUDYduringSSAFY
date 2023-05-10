<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <h1>Cat Image</h1>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="" id="catImg">
    <br>
    <button @click="getCatImg">Get Cat</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'HomeView',
  data(){
    return {
      imgSrc: null,
      message: "식빵굽는중.....",
      // caturl: 'https://api.thecatapi.com/v1/images/search'
    }
  },
  methods:{
    getCatImg(){
      console.log('되나?')
      const caturl = 'https://api.thecatapi.com/v1/images/search'
      axios({
        method:'get',
        url: caturl
      })
      .then((response)=>{
        console.log('되나!!!!')
        const caturl = response.data[0].url
        this.imgSrc = caturl
      })
      .catch((error)=>{
        console.log(error)
        console.log('왜 안됨')
      })
    }
  },
  created(){
    this.getCatImg()
  }
}
</script>
<style scoped>
  #catImg{
    display: inline-block;
    /* width: 200px; */
    height: 200px;
  }
</style>