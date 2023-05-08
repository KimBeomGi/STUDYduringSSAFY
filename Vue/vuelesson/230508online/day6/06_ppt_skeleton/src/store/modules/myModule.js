const myModule = {
  state : {
    level: 20,
  },
  mutations : {

  },
  actions: {
    incrementLevel(context) {
      context.commit('INCREMENT_Level')
    }
  },
}

export default myModule