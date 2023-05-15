<template>
  <div>
    <div class="card space" style="width: 18rem;">
      <img :src="`https://image.tmdb.org/t/p/w500/${moviecard?.poster_path}`" class="card-img-top" alt="">
      <!-- <img src=""  alt=""> -->
      <div class="card-body ">
        <h5 class="card-title">{{moviecard?.title}}</h5>
        <p class="card-text">{{moviecard?.overview}}</p>
        <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
      </div>
    </div> 
  </div>
</template>

<script>
export default {
  props:{
    moviecard: Object,
  }
}
</script>

<style>
.space{
  margin-right: 4rem
}
</style>