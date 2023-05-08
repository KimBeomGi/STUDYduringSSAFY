<template>
  <div>
    <li>
      <input type="checkbox" :checked="todo.isCompleted" @click="onClickCheckbox">
      <span :class="{done:todo.isCompleted}">{{ todo.content }}</span>
    </li>
  </div>
</template>

<script>
export default {
  name : 'TodoListItem',
  props : {
    todo : Object,
  },
  methods : {
    onClickCheckbox(){
      // 현재 todo요소의 isCompleted 속성 toggle
      // store의 todoList 변경을 요청
      // todo의 상태값을 바꿔서 새로운 todo 생성
      const new_todo = {
        // ...todo // spread 문법. 원래 todo가 가지고 있는 것을 그대로 가져온다는 뜻
        ...this.todo,
        isCompleted : !this.todo.isCompleted
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