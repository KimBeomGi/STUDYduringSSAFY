import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {      // data
    number : 0,
  },
  getters: {    // computed
    doubleOfNumber(state){
      return state.number * 2
    }
  },
  mutations: {  // state 변경
    // 각 함수는 인자를 2개 받는다.
    // 첫 번째 인자 state, 두 번째 인자 payload(데이터)
    ADD_NUMBER(state, num){
      state.number = state.number + num
    }
  },
  actions: {    // mutation 호출
    // 첫 번째 인자 context, 두 번째 인자 payload
    addNumber(context, payload){
      console.log(context)
      console.log(payload)
      // 액션에서는 비동기 요청이 가능하기 때문에 이렇게는 쓰지 말자.
      // context.state.number += payload
      // state 변경은 무조건 mutation
      context.commit('ADD_NUMBER', payload) //commit을 통해 mutations 호출
    },
  },
  modules: {
  }
})
