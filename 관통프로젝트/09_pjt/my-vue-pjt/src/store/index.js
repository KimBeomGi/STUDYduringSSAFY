import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import _ from 'lodash'

const API_URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=2b46fb99f88138f86fc6c767ebe959ec&language=ko-KR&page=3'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cards: [],
    WM_list: [],
    randomindex : 0,
    randomvalue : null,
  },
  getters: {
  },
  mutations: {
    GET_CARDS(state,cards){
      state.cards = cards
    },
    RANDOM_CARD(state,cards){
      state.cards = cards
      state.randomindex = _.sample(Object.keys(state.cards.results))
      state.randomvalue = state.cards.results[state.randomindex]
      // console.log(state.cards)
      // console.log(state.randomindex)
      // console.log(state.cards.results[state.randomindex])
    },
    CREATE_WM(state,wm){
      state.WM_list.push(wm)
    },
    UPDATE_WM(state,wm){
      state.WM_list = state.WM_list.map((el)=>{
        if(el.id == wm.id){
          return wm
        }else{
          return el
        }
      })
    },
    
  },
  actions: {
    getCards(context){
      axios({
        methods: 'get',
        url : `${API_URL}`
      })
      .then((res)=>{
        context.commit('GET_CARDS',res.data.results)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    random_card(context){
      axios({
        methods: 'get',
        url : `${API_URL}`
      })
      .then((res)=>{
        context.commit('RANDOM_CARD',res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    createWM({commit}, content){
      const dueDate = new Date()
      dueDate.setHours(0)
      dueDate.setMinutes(0)
      dueDate.setTime(0)
      const new_wm = {
        id : new Date().getTime(),
        dueDateTime : dueDate.toString(),
        content : content,
        isCompleted: false
      }
      commit('CREATE_WM',new_wm)
    },
    updateWM({commit},wm){
      commit('UPDATE_WM',wm)
    }
  },
  modules: {
  }
})
