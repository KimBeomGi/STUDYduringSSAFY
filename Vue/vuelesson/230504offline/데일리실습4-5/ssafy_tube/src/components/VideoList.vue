<template>
  <ul class="p-0 ms-3" >

    <VideoListItem 
    v-for="video in videoList" :key="video.id.videoId"
    :video-item="video"
    @click="onClick"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name : 'VideoList',
  props:{
    videoList : Array   // 왼쪽은 받아올때: 오른쪽은 데이터 타입
  },
  components:{
    VideoListItem
  },
  methods:{
    onClick(selectedItem){
      this.$emit('item-click', selectedItem)
    }
  },
}
</script>

<style>

</style>