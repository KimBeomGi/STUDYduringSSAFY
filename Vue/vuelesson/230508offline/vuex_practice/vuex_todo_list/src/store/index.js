import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[createPersistedState(),],
  state: {
    todoList : [],
  },
  getters: {
    allList(state){
      return state.todoList
    },
  },
  mutations: {
    ADD_TODO(state, todo){
      state.todoList.push(todo)
    },
    UPDATE_TODO(state,todo){
      // todoList를 수정, 원래 있던 요소들은 그대로 남기고,
      // 바뀐 요소만 갈아 끼우기..
      // map : 각 요소에 대해서 반환 값을 이용해서 새로운 배열 생성
      // 수정되지 않은 요소는 그대로 반환, 수정된 요소는 수정요소를 반환
      state.todoList = state.todoList.map((origin)=>{
        if(origin.date == todo.date){ //수정된 요소
          return todo
        }else{
          return origin
        }
      })
    }
  },
  actions: {
    // addTodo({commit}, ){    // 구조 분해 할당! ES6의 문법 중 하나임
    //   commit('ADD_TODO')
    // }
    addTodo(context, content){
      const new_todo = {
        isCompleted : false,
        content : content,
        date : new Date().getTime()
      }
      context.commit('ADD_TODO', new_todo)
    },
    updateTodo(context, todo){
      context.commit('UPDATE_TODO', todo)
    },
  },
  modules: {
  }
})
