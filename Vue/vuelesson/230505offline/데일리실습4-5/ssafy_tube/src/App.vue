<template>
  <div id="app" class="cast">
    <div>
      <h1 class="text-primary">SSAFY TUBE</h1>
      <SearchBar @search="onSearch"/>
    </div>
    <!-- justify-content-around -->
    <div class="d-flex flex-row " style="width : 80%" >
      <div style="width : 40 %;">
        <VideoDetail v-if="selectedVideo" :selected-video="selectedVideo"/>
        <div v-else class="empty-detail">
          <div style="height : 70%;">
            <img src ="./assets/noResult.png" alt="" style="height : 100%">
          </div>
          <div style="height : 30%;">
            <h4>선택된 비디오가 없습니다!</h4>
            <h4>비디오를 검색하시거나 리스트에서 골라주세요!</h4>
          </div>
        </div>
      </div>
      <div style="width : 60 %;">
        <VideoList :video-list="videoList"
        @item-click="onItemClick"
        />
      </div>
    </div>
    <!-- <ul>
      <li v-for="video in videoList" :key="video.id.videoId">
        <img :src="video.snippet.thumbnails.default.url" alt="">
      </li>
    </ul> -->
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'
import axios from 'axios'   // axios 사용하려면 npm install axios를 쓰자

export default {
  name: 'App',
  components: {
    SearchBar,VideoDetail,VideoList,
  },
  data(){
    return{
      videoList : [],
      selectedVideo : null,
    }
  },
  methods:{
    onItemClick(selectedItem){
      this.selectedVideo = selectedItem
    },
    onSearch(keyword){
      // 하위 요소로부터 발생하는 이벤트 처리
      this.search(keyword)

    },
    search(keyword){
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      
      // API 요청해서 데이터 받아와서 this.videoList에 추가
      axios({
        url: API_URL,
        params : {
          key : 'AIzaSyAMizXcBgpkxeZn2O4Dg8j4y340mPRL3Xk', //개인 API키를 이용하면 됨
          part : 'snippet',
          type : 'video',
          q : keyword,
        }
      })
      .then((response)=>{
        // console.log(response.data.items)
        this.videoList = response.data.items
      })
    }
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
  margin-top: 60px;
}
.empty-detail{
  width: 500px;
  height: 500px;
}
.cast{
  width: 1300px;
  height: 500px;
  margin: auto;
}
</style>
