<template>
  <div class="home">
    <h1>Home</h1>
    <button @click="goCreate">글쓰기</button>
    <!-- 게시글 목록 출력 -->
    <ArticleItem v-for="article in articles"
    :key="article.id"
    :article="article" />
  </div>
</template>

<script>
import ArticleItem from '../components/ArticleItem'

export default {
  name: 'HomeView',
  components: {
    ArticleItem,
  },
  computed : {
    articles(){
      return this.$store.state.articles
    }
  },
  created(){
    console.log(this)
  },
  methods:{
    goCreate(){
      this.$router.push({name:'create'})
    },
  }
}
</script>
