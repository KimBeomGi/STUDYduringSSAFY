<template>
  <div id="app">
    <h1>길이 {{ messageLength }}의 메시지 {{ message }}를 입력받음</h1>
    <h3>x2 : {{ doubleLength }}</h3>
    <!-- <input type="text" @keyup.enter="changeMessage" v-model="inputData"> -->
    <h1>{{ level }}</h1>
    <button @click='uplevel'>levelup</button>
    <input type="text" @keyup.enter="onSubmit" v-model="inputData">
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'App',
  components: {
  },
  created(){
    this.$store.dispatch('loadMessage')
    console.log(this.$store)
  },
  computed: {
    // message() {
    //   return this.$store.state.message
    // },
    ...mapState(['message']),
    ...mapState({
      msg: state => state.message,
      level: state => state.myModule.leve,
    }),
    // messageLength() {
    //     return this.$store.getters.messageLength
    // },
    // doubleLength() {
    //     return this.$store.getters.doubleLength
    // },
    ...mapGetters(['messageLength', 'doubleLength'])
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    // changeMessage() {
    //   const newMessage = this.inputData
    //   this.$store.dispatch('changeMessage', newMessage)
    //   this.inputData = null
    // },
    // loadMessage(context){
    //   context.commit('LOAD_MESSAGE')
    // }
    // ...mapActions(['changeMessage'])
    ...mapActions({
      actionsChangeMessage: 'changeMessage',
      uplevel: 'incrementLevel'
    }),
    onSubmit(){
      const newMessage = this.inputData
      this.actionsChangeMessage(newMessage)
      this.inputData = null
    },
    uplevel(){
      this.$store.dispatch('incrementLevel')
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
