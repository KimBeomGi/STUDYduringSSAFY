<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>버튼 박스 제작</h1>
    <h2>예약 페이지</h2>
    <h3>시간 선택</h3>
    <table>
      <tbody>
        <thead>
        </thead>
        <tr v-for="(line,index) in times" :key="index">
          <td v-for="time in line" :key="time" @click='toggleSelect(time)' :class="{selectcolor: isSelected(time)}">
            <!-- <button id="timebutton" @click='toggleSelect(time)' :class="{selectcolor: time.isCompleted}">{{time}}</button> -->
            <button class="timebutton" >{{time}}</button>
          </td>
        </tr>
      </tbody>
    </table>
    <hr id='undertablehr'>
    <h3>선택시간: {{ sortedTimes }}</h3>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import _ from 'lodash'
export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data(){
    return {
      times: [
        ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30"],
        ["14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30"],
        ["19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30"]
      ],
      selectedTimes: [],
    }
  },
  methods: {
    
    // toggleSelect(time) {
    //   if (this.selectedTimes.length >= 5) {
    //     alert("5개 이상 선택할 수 없습니다.");
    //   } else {
    //     const index = this.selectedTimes.indexOf(time);
    //     if (index !== -1) {
    //       // 이미 선택된 시간인 경우 선택 해제
    //       this.selectedTimes.splice(index, 1);
    //       time.isCompleted = false;
    //     } else {
    //       // 선택되지 않은 시간인 경우 선택
    //       this.selectedTimes.push(time);
    //       time.isCompleted = true;
    //     }
    //   }
    // },
    toggleSelect(time) {
      if (this.selectedTimes.length >= 5 && !this.selectedTimes.includes(time)) {
        alert('5개 이상 선택할 수 없습니다.')
      } else {
        const index = this.selectedTimes.indexOf(time)
        if (index !== -1) {
          this.selectedTimes.splice(index, 1)
        } else {
          this.selectedTimes.push(time)
        }
      }
    },
    isSelected(time) {
      return this.selectedTimes.includes(time)
    }
  },
  computed:{
    sortedTimes: function(){
      return _.sortBy(this.selectedTimes).join(', ')
    }
  }
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
table{
  text-align: center;
  width: 75%;
  text-align : center;
  margin: 0 auto;
}
table th{
  padding : 10px;
  border-bottom: 2px solid  darkgray;
}
table td{
  padding : 10px;
  align-items: center;
}
#undertablehr{
  width: 60%;
}
.timebutton{
    background-color:transparent;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 0px solid;
    cursor: pointer;
    margin: 0;
    padding: 0;
}
.selectcolor{
  background-color: skyblue;
}
</style>
