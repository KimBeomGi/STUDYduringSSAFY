<template>
  <li>
    <input type="checkbox" :checked="todo.isCompleted" @click="onClickCheckBox">
    <span :class="{done:todo.isCompleted}">{{ todo.content }}</span>
  </li>
</template>

<script>
export default {
  name : 'TodoListItem',
  props: {
    todo : Object,
  },
  methods : {
    onClickCheckBox(){
      const new_todo = {
        ...this.todo,
        isCompleted : !this.todo.isCompleted
      }
      this.$store.dispatch('updateTodo', new_todo)
    }
  }
}
</script>

<style>
  .done{
    text-decoration: line-through;
    color: gray;
  }
</style>