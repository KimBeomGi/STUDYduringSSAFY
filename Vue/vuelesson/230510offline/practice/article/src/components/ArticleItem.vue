<template>
  <div>
      <p><span class='pointer' @click="goDetail">제목 : {{ article.title }}</span></p>
      <!-- <p>내용 : </p>
      <p>{{ article.content }}</p>
      <p>작성일 : {{createdAt}}</p> -->
  </div>
</template>

<script>
export default {
  name : 'ArticleItem',
  props : {
    article : Object,
  },
  methods:{
    goDetail(){
      this.$router.push({name:'detail',params:{articleId:this.article.id}})
    }
  },
  computed : {
    createdAt(){
      return new Date(this.article.createdAt).toString()
    }
  }
}
</script>

<style>
  .pointer{
    cursor: pointer;
  }
</style>