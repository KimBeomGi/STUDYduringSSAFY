const state = () => {
  return {
		// todo 리스트 Array
    list: [
			// 개별 todo Object
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2023-05-09T00:00',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,				        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2023-05-09T00:00',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2023-05-11T00:00',
        isCompleted: true,
        isImportant: false,
      },
    ],
  }
}
//state 변경을 하려면 action 호출해서 mutation 실행되도록 
const mutations = {
  UPDATE_TODO(state,todo){
    state.list = state.list.map((el)=>{
      if(el.id == todo.id){
        return todo
      }else{
        return el
      }
    })
  },
  CREATE_TODO(state,todo){
    state.list.push(todo)
  }
}
const actions = {
  updateTodo({commit},todo){
    commit('UPDATE_TODO',todo)
  },
  createTodo({commit}, content){
    const dueDate = new Date()
    dueDate.setHours(0)
    dueDate.setMinutes(0)
    const new_todo = {
      id  : new Date().getTime(),
      dueDateTime : dueDate.toString(),
      content : content,
      isCompleted: false,
      isImportant: false,
    }
    commit('CREATE_TODO',new_todo)
  },
}
const getters = {
  importantList(state){
    return state.list.filter((el)=>{
      return el.isImportant
    })
  },
  todayList(state){
    return state.list.filter((todo)=>{
      //오늘 날짜가 필요합니다. 
      const today = new Date()
      const todoDate = new Date(todo.dueDateTime)
      //오늘 날짜와 연,월, 일이 다 똑같으면 해당 요소 포함
      const isSameYear = today.getFullYear() == todoDate.getFullYear()
      const isSameMonth = today.getMonth() == todoDate.getMonth()
      const isSameDate = today.getDate() == todoDate.getDate()
      return isSameDate && isSameYear && isSameMonth
    })
  },
}
export default{
  state,
  mutations,
  actions,
  getters,
}