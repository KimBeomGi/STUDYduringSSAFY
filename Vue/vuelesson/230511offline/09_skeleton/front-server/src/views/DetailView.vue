<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="goHome">목록으로</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DetailView',
  data() {
    return{
      article : null
    }
  },
  created() {
    // 컴포넌트가 만들어지면...
    // 상세게시글을 서버에서 조회하기
    this.getArticle()
  },
  methods: {
    goHome(){
      this.$router.push({name:'ArticleView'})
    },
    getArticle(){
      //서버에다가 요청하고... 응답받아서 this.article에 넣어주기
      axios({
        method : 'get',
        url : `http://localhost:8000/api/v1/articles/${this.$route.params.id}/`
      })
      .then((response)=>{
        this.article = response.data
        // console.log(response)
      })
      .catch((error)=>{
        console.log(error)
      })
      this.article = ''
    }
  }
}
</script>
