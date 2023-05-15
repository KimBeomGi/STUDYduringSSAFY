<template>
    <div>
      <div class= "d-flex flex-wrap justify-content-center">
        <MovieCardItem @click="goWatchList"
        v-for="moviecard in cards" :key="moviecard.id" 
        :moviecard="moviecard"
        />
      </div>
    </div>
</template>

<script>
import MovieCardItem from '@/components/MovieCardItem'

export default {
  name : 'MovieCard',
  components:{
    MovieCardItem,
  },
  computed:{
    cards(){
      return this.$store.state.cards
    }
  },
  methods:{
    goWatchList(){

    }
  },
  
}
</script>

<style>

</style>