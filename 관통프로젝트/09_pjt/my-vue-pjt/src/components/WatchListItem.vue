<template>
  <div class ="pt-2 bg-secondary bg-opacity-10"  :class="{ 'bg-opacity-25': bgColor }" @click="changeBackground">
    <div :class="{ done: wm.isCompleted }" @click=toggleCompleted>{{ wm.content }}</div>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  data() {
    return {
      isClicked: false,
    };
  },
  props: {
    wm: Object,
  },
  computed: {
    bgColor() {
      return this.isClicked;
    },
  },
  methods: {
    toggleCompleted() {
      const new_wm = {
        ...this.wm,
        isCompleted: !this.wm.isCompleted,
      };
      this.$store.dispatch('updateWM', new_wm);
    },
    changeBackground() {
      this.isClicked = !this.isClicked;
    },
  },
};
</script>

<style>
.done {
  text-decoration: line-through;
  color: gray;
}
</style>
