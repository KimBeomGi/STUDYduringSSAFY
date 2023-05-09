<template>
  <div>
    <h1>전체 할 일</h1>
    <TodoList
    :todo-list="todoList"
    />
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
export default {
  name : 'AllTodoPage',
  components : {
    TodoList,
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