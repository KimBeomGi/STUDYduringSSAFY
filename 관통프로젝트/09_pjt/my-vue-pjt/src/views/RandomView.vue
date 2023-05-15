<template>
  <div>
    <button @click="offInterval" style="width:285px; height:100px" class="mt-5">멈춰!</button>
    <div class = "d-flex justify-content-center">
      
    <div class="card" style="width: 18rem;">
      <img :src="`https://image.tmdb.org/t/p/w500/${moviecard?.poster_path}`" class="card-img-top" alt="">
      <!-- <img src=""  alt=""> -->
      <div class="card-body">
        <h5 class="card-title">{{moviecard?.title}}</h5>
        <p class="card-text">{{moviecard?.overview}}</p>
        <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
      </div>
      
      
    </div> 
  </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name : 'RandomView',
  data(){
      return{
        // randomindex : 0
        num : 0,
        role : null,
        moviecard : null,
      }
    },
  computed:{
    // moviecard(){
    //   // this.$store.dispatch('random_card')
    //   return this.$store.state.randomvalue
    // }
  },
  methods:{
    // getRandomIndex(){
    //   this.randomindex=_.sample(Object.keys(this.$store.state.cards.results))
    // },
    onInterval(){
      this.role = setInterval(()=>{
        this.moviecard = _.sample(this.$store.state.cards)
      }, 0.001)
    },
    offInterval(){
      clearInterval(this.role)
    }
  },
  created(){
    // this.$store.dispatch('random_card')
    this.onInterval()
  }
}
</script>

<style>

</style>