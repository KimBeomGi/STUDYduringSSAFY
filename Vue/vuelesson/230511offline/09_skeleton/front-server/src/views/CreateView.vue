<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="onSubmit">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return{
      title : '',
      content : '',
    }
  },
  methods: {
    onSubmit(){
      // event.preventDefault()
      // 얘가.. 글쓰기 요청
      //post 요청 보내면 됨
      const data = new FormData()
      data.append('title',this.title)
      data.append('content',this.content)
      axios({
        method : 'POST',
        url : 'http://127.0.0.1:8000/api/v1/articles/',
        data,
      })
      .then(()=>{
        // console.log(response.data)
        this.$router.push({name: 'ArticleView'})
      })
      .catch((error)=>{
        alert('무엇??')
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>
