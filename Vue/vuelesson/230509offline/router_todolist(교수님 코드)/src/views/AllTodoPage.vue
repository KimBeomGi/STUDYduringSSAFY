<template>
  <div>
    <h1>전체 할 일</h1>
    <TodoForm/>
    <TodoList
    :todo-list="todoList"/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
export default {
  name : 'AllTodoPage',
  components : {
    TodoList,
    TodoForm
  },
  computed : {
    todoList(){
      return this.$store.state.todo.list
    }
  }
}
</script>

<style>

</style>