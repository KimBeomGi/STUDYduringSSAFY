<template>
  <div>
    <ul>
      <TodoListItem v-for="todo in todoList"
      :key="todo.date"
      :todo="todo"
      />

    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
  name : 'TodoList',
  components : {
    TodoListItem,
  },
  computed : {
    todoList(){
      return this.$store.state.todoList
    }
  }

}
</script>

<style>

</style>