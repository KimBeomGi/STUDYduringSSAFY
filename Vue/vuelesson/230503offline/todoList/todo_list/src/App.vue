<template>
  <div id="app">
    <h1>오늘의 할 일</h1>
    <p>
      <input type="text" v-model="content">
      <button @click="addTodo">+</button>
    </p>
      <!-- 할 일 목록 -->
      <TodoList
      :todo-list="todoList"
      @click-check-box="handleCheckEvent"
      />
    <p>
      <button @click="deleteDone">완료 목록 삭제</button>
    </p>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  data(){
    return{
      todoList : [],
      content : '',
    }
  },
  components: {
    TodoList,
  },
  methods : {
    deleteDone(){
      this.todoList = this.todoList.filter((element) => {
        if(element.isCompleted){
          return false
        }
        else{
          return true
        }
      })
    },
    addTodo(){
      const todo = {
        isCompleted : false,
        content : this.content,
        date : new Date().getTime(),
      }
      this.todoList.push(todo)
      this.content=''
    },
    handleCheckEvent(todo){ //이벤트가 발생한 todo 요소의 상태를 반대로 바꿔주면됨
      this.todoList.forEach((element)=>{
        if (element == todo){
          element.isCompleted = !element.isCompleted
          // 엘리먼트 자체를 바꿔 끼우면 되나?
          // 안되나?
        }
      })
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
