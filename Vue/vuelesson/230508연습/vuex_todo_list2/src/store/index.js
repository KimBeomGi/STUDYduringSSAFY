import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[createPersistedState()],
  state: {
    todoList : [],
  },
  getters: {
    allList(state){
      return state.todoList
    }
  },
  mutations: {
    ADD_TODO(state,todo){
      state.todoList.push(todo)
    },
    UPDATE_TODO(){
      state.todoList = state.todoList.map((origin) => {
        if(origin.date == todo.date){
          return todo
        }else{
          return origin
        }
      })
    },
  },
  actions: {
    addTodo(context,content){
      const new_todo = {
        isCompleted : false,
        content : content,
        date : new Date().getTime()
      }
      context.commit('ADD_TODO',new_todo)
    },
    updateTodo(context,todo){
      context.commit('UPDATE_TODO',todo)  
    }
  },
  modules: {
  }
})
