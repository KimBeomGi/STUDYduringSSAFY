<template>
    <div>
      <MovieCard />
    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
export default {
  name : 'MovieView',
  components:{
    MovieCard,
  },
  methods:{
    getCards(){
      this.$store.dispatch('getCards')

    }
  },
  created(){
    this.getCards()
  }
}
</script>

<style>

</style>