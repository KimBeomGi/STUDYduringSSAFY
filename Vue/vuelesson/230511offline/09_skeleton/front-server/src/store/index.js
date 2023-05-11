import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
      // {
      //   id: 1,
      //   title: '제목',
      //   content: '내용'
      // },
      // {
      //   id: 2,
      //   title: '제목2',
      //   content: '내용2'
      // },
    ],
  },
  getters: {
  },
  mutations: {
    SET_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    getArticles(context){
      console.log(context)
      console.log('store getArticles Action...')
      //서버에 요청해서 articles 받아와서 state.articles에 저장
      axios({
        method: 'get',
        url : 'http://localhost:8000/api/v1/articles/'
      })
      .then((response)=>{
        // response.data > 얘가 articles Array에요
        context.commit('SET_ARTICLES',response.data)
        
      })
      .catch((error)=>{
        console.log(error)
      })
      // context.commit('SET_ARTICLES',articles)
    }
  },
  modules: {
  }
})
