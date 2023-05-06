<template>
  <div class="mb-5">
		<input class="border-primary rounded" style="width: 500px;" type="text" placeholder="검색할 내용을 입력하세요" v-model.trim="keyword" @keyup.enter="onSearch">
		<button type="button" class="btn btn-primary ms-2 p-0" @click="onSearch" >🔍검색🔍</button>
  </div>
</template>

<script>
export default {
  name:'SearchBar',
	data(){
		return{
			keyword : '',
		}
	},
	methods:{
		onSearch(){
			// 검색어를 상위 모듈로 전달
			if(this.keyword){
				this.$emit('search', this.keyword)
			}
			else{
				alert('빈 검색어입니다. 검색어를 입력하세요')
			}
			this.keyword = ''
		}
	}
}
</script>

<style>
.input_border {
	width:500px;
	border-color: rgba(0, 0, 255, 0.705);
}
</style>