<template>
  <div @click="itemSelected">
    <h5>PK : {{ article.id }}</h5>
    <p>제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props:{
    article : Object
  },
  methods : {
    itemSelected(){
      //아이템이 선택되었으니, 상세화면으로 이동
      this.$router.push({name:'DetailView', params:{id:this.article.id}})
    }
  }
}
</script>

<style>

</style>
