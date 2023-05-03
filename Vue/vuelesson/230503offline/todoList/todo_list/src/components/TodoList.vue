<template>
  <div>
    <ul>
      <TodoListItem v-for="todo in todoList" :key="todo.date"
        :todo="todo"
        @click-check-box="handleCheckEvent"
      />
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
    name:'TodoList',
    props : {
        todoList : Array
    },
    components : {
        TodoListItem,
    },
    methods:{
      handleCheckEvent(todo){
        this.$emit('click-check-box',todo)
      }
    },
}
</script>

<style>

</style>