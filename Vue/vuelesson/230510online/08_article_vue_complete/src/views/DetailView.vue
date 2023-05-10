<template>
  <div>
    <h1>Detail</h1>
    <!-- ?는 optional chaning 값이 없다해도 글 번호: 제목: 등은 잘 뜰 수 있게 하기위함 -->
    <!-- ES2020에 추가 된 문법 -->
    <p>글 번호 : {{article?.id}}</p>
    <p>제목 : {{article?.title}}</p>
    <p>내용 : {{article?.content}}</p>
    <!-- <p>작성시간 : {{article?.createdAt}}</p> -->
    <p>작성시간 : {{ articleCreatedAt }}</p>
    <button @click="deleteArticle">삭제</button><br>

    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },  
    articleCreatedAt(){
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      // Date 객체 1970년 1월 1일 기준 1초씩 세서 현재의 날자를 알려줌.
      // 밀리초를 정수로 해서 컴퓨터에서 숫자를 날짜로 변환.
      return createdAt
    }
  },
  methods: {
    getArticleById(id) {
      // const id = this.$route.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      if (!this.article) {
        this.$router.push({ name: 'NotFound404' })
      }
    },
    deleteArticle(){
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name: 'index' })
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }
}
</script>