<template>
  <div class="d-flex flex-row align-itmes-center" @click="onClick">
    <img :src="videoItem.snippet.thumbnails.default.url" alt="">
    <span v-html="videoItem.snippet.title"></span>
  </div>
</template>

<script>
export default {
  name : 'VideoListItem',
  props :{
    videoItem : Object,
  },
  methods:{
    onClick(){
      this.$emit('click', this.videoItem) // click 이벤트 발생했다 상위요소에 알려주기
    }
  },
}
</script>

<style>

</style>