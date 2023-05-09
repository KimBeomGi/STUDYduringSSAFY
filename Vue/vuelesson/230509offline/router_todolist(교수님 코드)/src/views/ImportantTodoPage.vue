<template>
  <div>
    <h1>중요 할 일</h1>
    <TodoForm/>
    <TodoList 
    :todo-list="importantList" />
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
export default {
  name : 'ImportantTodoPage',
  components : {
    TodoList,
    TodoForm
  },
  computed : {
    importantList(){
      return this.$store.getters.importantList
    }
  }
}
</script>

<style>

</style>