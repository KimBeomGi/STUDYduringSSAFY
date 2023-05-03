<template>
  <div>
    <h1>AppParent</h1>
      <input type="text" v-model="childData" @keyup.enter="emitchildInputEvent">
      <p>App Data : {{ appData }}</p>
      <p>Parent Data : {{ parentData }} </p>
  </div>
</template>

<script>
export default {
  name : 'AppChild',
  data(){
    return{
      childData : '',
    }
  },
  props:{
    appData:String,
    parentData:String,
  },
  // 하위 요소에서 상위요소로 데이터를 전달 하는 방법
  // 이벤트를 이용하기, 직접전달이 안되어서 이벤트 발생시켜서, 데이터도 같이 던지기
  // 부모요소에서는 하위요소에서 이벤트가 발생하면 데이터를 가져오도록 처리
  // 사용자가 input요소에 데이터를 입력하면
  // 그때 이벤트 발생시키기
  methods:{
    emitchildInputEvent(){
      // 이벤트를 발생시키는 메서드
      // this.$emit()이렇게 해야 이벤트가 발생함
      this.$emit('child-input', this.childData)
      this.childData = ''
    }
  }
}
</script>

<style>

</style>