<template>
  <div>
    <label>완료 : <input type="checkbox" :checked='todo.isCompleted'></label>
    <label>중요 : <input type="checkbox" :checked='todo.isImportant'></label>
    <span :class="{done:todo.isCompleted}">
      {{ todo.content }}
    </span>
  </div>
</template>

<script>
export default {
  name:'TodoListItem',
  props : {
    todo: Object
  },
  methods : {
    toggleCompleted(){
      const new_todo = {
        ...this.todo,
        isCompleted : this.todo.isCompleted
      }
      this.$store.dispatch('updateTodo', new_todo)
    },
    toggleImportant(){
      const new_todo = {
        ...this.todo,
        isImportant : this.todo.isImportant
      }
      this.$store.dispatch('updateTodo', new_todo)
    },
  }
}
</script>

<style>
  .done{
    text-decoration: line-through;
    color: gray;
  }
</style>