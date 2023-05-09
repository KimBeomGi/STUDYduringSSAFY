<template>
  <div>
    <h1>오늘 할 일</h1>
    <TodoForm/>
    <TodoList
    :todo-list="todayList"/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name : 'TodayTodoPage',
  components : {
    TodoList,
    TodoForm,  
  },
  computed : {
    todayList(){
      return this.$store.getters.todayList
    }
  }
}
</script>

<style>

</style>