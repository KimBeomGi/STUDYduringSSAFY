import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articleSequence : 4,
    articles : [
      {
        id : 1,
        title : '제목 1',
        content : '내용 1',
        createdAt : new Date().getTime()
      },
      {
        id : 2,
        title : '제목 2',
        content : '내용 2',
        createdAt : new Date().getTime()
      },
      {
        id : 3,
        title : '제목 3',
        content : '내용 3',
        createdAt : new Date().getTime()
      },
    ]
  },
  getters: {
  },
  mutations: {
    ADD_ARTICLE(state,article){
      state.articles.unshift(article)
      state.articleSequence += 1
    }
  },
  actions: {
    // addArticle({commit},article){
    addArticle(context,payload){
      console.log(context)
      //title, content
      const article = {
        id : context.state.arrticleSequence,
        title : payload.title,
        content : payload.content,
        createdAt : new Date().getTime()
      }
      context.commit('ADD_ARTICLE', article)
    }
  },
  modules: {
  }
})
