<template>
  <div class="mx-auto" style="width : 80%;">
    <WatchListForm/>
    <WatchListItem v-for="wm in wmList" :key="wm.id"
    :wm="wm"/>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  components:{
    WatchListForm,
    WatchListItem
  },
  computed : {
    wmList(){
      return this.$store.state.WM_list
    }
  },
}
</script>

<style>

</style>