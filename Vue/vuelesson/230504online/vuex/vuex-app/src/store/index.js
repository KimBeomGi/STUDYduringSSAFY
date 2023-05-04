import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message : 'message in store'
  },
  getters: {
    meessageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.meessageLength * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      // console.log(state)
      // console.log(message)
      state.message = message
    }
  },
  actions: {
    changeMessage(context, message){
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
