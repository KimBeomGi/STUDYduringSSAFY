<template>
  <div class='video'>
    <h1>선택된 비디오</h1>
    <div>
      <iframe id="inlineFrameExample"
        :src="videoSrc">
      </iframe>
      <!-- {{ selectedVideo }} -->
    </div>
    <div>
      <h3>제목</h3>
      <p v-html="videoTitle"></p>
      <p>설명</p>
      <p v-html="videoDescription"></p>
    </div>
  </div>

</template>

<script>
export default {
  name : 'VideoDetail',
  props : {
    selectedVideo : Object
  },
  computed:{
    videoSrc(){
      // const videoId = this.selectedVideo ? this.selectedVideo.id.video :''
      return `https://www.youtube.com/embed/${this.selectedVideo.id.video}`
    },
    videoTitle(){
      return this.selectedVideo.snippet.title
    },
    videoDescription(){
      return this.selectedVideo.snippet.description
    }
  }
}
</script>

<style>
  .class{
    width: 500px;
    height: 500px;
  }
</style>