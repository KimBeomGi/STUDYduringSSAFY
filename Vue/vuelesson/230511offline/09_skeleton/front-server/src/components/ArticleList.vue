<template>
  <div class="article-list">
    <h3>Article List</h3>
    <!-- article List 가져와서 반복문 돌리기 -->
    <ArticleListItem
    v-for="article in articles" :key="article.id"
    :article="article"
    />

  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem
  },
  computed: {
    articles(){
      return this.$store.state.articles
    },
  },
  created(){
    // 화면이 만들어지면...
    // api서버에 리스트를 요청해서
    // 리스트를 받아와서 store에 저장하면 됩니다.
    this.$store.dispatch('getArticles')
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
