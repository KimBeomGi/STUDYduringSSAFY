<template>
  <li>
		<input type="checkbox" :checked="todo.isCompleted" @click='handleCheckEvent'>
		<span :class="{completed:todo.isCompleted}">{{ todo.content }}</span>
  </li>
</template>

<script>

export default {
	name:'TodoListItem',
	props : {
		todo : Object
	},
	methods:{
		handleCheckEvent(){
			this.$emit('click-check-box', this.todo)
		}
	}
}
</script>

<style>
	.completed{
		text-decoration: line-through;
		color: yellow;
	}
</style>