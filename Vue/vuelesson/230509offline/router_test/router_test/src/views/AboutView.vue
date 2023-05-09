<template>
  <div class="about">
    <!-- {{ $route.params.userName}} -->
    {{ userName }}
    <h1>This is an about page</h1>
    <button @click='buttonClick'>홈으로 이동</button>
  </div>
</template>
<script>
export default {
  name: 'AboutView',
  methods : {
    buttonClick(){
      // 자바스크립트 코드로 라우팅 하기
      // this.$router.push('/')
      this.$router.push({name:'home'})
    }
  },
  computed:{
    userName(){
      return this.$route.params.userName
    }
  }
}
</script>