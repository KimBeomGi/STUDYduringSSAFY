<template>
  <div>
    <router-link :to="{name : 'AllTodoPage'}">전체</router-link> |
    <router-link :to="{name : 'TodayTodoPage'}">오늘</router-link> |
    <router-link :to="{name : 'ImportantTodoPage'}">중요</router-link> |
  </div>
</template>

<script>
export default {
  name : 'SideBar',

}
</script>

<style>
  #side-bar{
    border: 2px solid black;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 3px;
  }
</style>