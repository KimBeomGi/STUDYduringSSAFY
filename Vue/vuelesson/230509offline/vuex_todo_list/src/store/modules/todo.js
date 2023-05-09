const state = () => {
  return {
        // todo 리스트 Array
    list: [
            // 개별 todo Object
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2021-12-09T00:00',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,				        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-10T00:00',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T00:00',
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
}
const actions = {
  updateTodo({commit},todo){
    commit('UPDATE_TODO', todo)
  },
}
const getters = {
  importantTodoList(state){
    return state.list.filter((el)=>{
      return el.isImportant   
    })
  },
  todayList(state){
    return state.list.filter((todo)=>{
      // 오늘 날짜가 필요합니다.ㄴ
      const today = new Date()
      const todoDate = new Date(todo.dueDateTime)
      // 오늘 날자와 연, 월, 일이 다 똑같으면 해당 요소 포함
      const isSameYear = today.getFullYear() == todoDate.getFullYear)
      const isSameYear = today.getFullYear() == todoDate.getFullYear)
      const isSameYear = today.getFullYear() == todoDate.getFullYear)
      return issAME dATE[]

    })
  }
}

export default{
  state,
  mutations,
  actions,
  getters,

}