<template>
  <div>
    <h1>중요 할 일</h1>
    <TodoList :todo-list="importantList"/>
  </div>
</template>

<script>
import TodoList from "@/components/TodoList"

export default {
  name : 'ImportantTodoPage',
  components:{
    TodoList
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