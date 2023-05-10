<template>
  <div>
    <h1>상세 화면</h1>
    <p>제목</p>
    <p>{{ article?.title }}</p>
    <br>
    <p>내용</p>
    <p>{{ article?.content }}</p>
    <button @click="goHome">목록으로</button>
  </div>
</template>

<script>
export default {
  name:'DetailView',
  // 함수 만들기, 그 함수를 컴포넌트가 만들어지면 호출
  data(){
    return{
      article : null
    }
  },
  methods : {
    goHome(){
      this.$router.push({name:'home'})
    },
    getArticle(){
      // id는 어디서????
      const id = Number(this.$route.params.articleId)
      for(const article of this.$store.state.articles){
        if(article.id == id){
          return article
        }
      } 
      this.$router.push({name:'notfound404'})
      return null
    }
  },
  created(){
    this.article = this.getArticle()  
  }
  // props로 받아오는게 아니라...
  // store에 id로 접근해서 가져오기

}
</script>

<style>

</style>