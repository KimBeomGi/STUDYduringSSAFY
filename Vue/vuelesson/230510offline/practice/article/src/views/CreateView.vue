<template>
  <div>
    <h1>글쓰기</h1>
    <form @submit.prevent="onSubmit">
      <p><label for="title">제목</label></p>
      <p><input type="text" id="title" v-model="title"></p>
      <br>
      <p><label for="content">내용</label></p>
      <p><textarea id="content" cols="30" rows="10" v-model="content"></textarea></p>
      <p><input type="submit" value="작성하기" ></p>
    </form>
    <router-link :to="{name:'home'}">목록으로</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data(){
    return{
      title : '',
      content : '',
    }
  },
  //form에 submit 이벤트가 발생하면... titlde, content 받아와서 action 수행 
  methods:{
    // onSubmit(event){
      // event.preventDefault() // 이것도 되고
    onSubmit(){
      // console.log('오어우오우')
      const payload = {
        title : this.title,
        content : this.content,
      }
      this.$store.dispatch('addArticle', payload)
      //홈으로 화면 이동
      this.$router.push({name:'home'})
    }
  }
}
</script>

<style>

</style>