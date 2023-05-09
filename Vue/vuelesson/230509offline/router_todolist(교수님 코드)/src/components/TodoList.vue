<template>
  <div>
    <ul>
      <TodoListItem v-for="todo in todoList" 
      :key="todo.id"
      :todo="todo"/>
    </ul>
  </div>
</template>

<script>

import TodoListItem from '@/components/TodoListItem'
export default {
  name : 'TodoList',
  props : {
    todoList : Array,
  },
  components : {
    TodoListItem,
  },

}
</script>

<style>

</style>