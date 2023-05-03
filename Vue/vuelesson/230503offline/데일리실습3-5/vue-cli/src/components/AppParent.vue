<template>
  <div>
      <h1>AppParent</h1>
      <input type="text" v-model='parentData ' @keyup.enter="emitParentInputEvent">
      <p>App Data :  {{ appData }}</p>
      <p>Child Data : {{ childData }} </p>
      <AppChild v-bind:app-data="appData" v-bind:parent-data="parentData"
      @child-input='handleChildInput'
      />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'
export default {
  name : 'AppParent',
  data(){
    return {
      parentData : '',
      childData : ''
    }
  },
  props:{
    appData : String,
  },
  components:{
    AppChild,
  },
  methods:{
    handleChildInput(childData){
      // console.log('하위요소에서 엔터키 누름')
      console.log(childData)
      this.childData = childData
      this.$emit('child-input', childData)
    },
    emitParentInputEvent(){
      this.$emit('parent-input', this.parentData)
    }
  },
}
</script>

<style>

</style>