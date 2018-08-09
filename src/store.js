export default {
  modules: {
    crocus: {
      strict: true,
      namespaced: true,
      state: {
        connectTime: -1,
        crocusUrl: 'www.crocus.co.kr',
        owner: 'Kwanwoo Ko'
      },
      mutations: {
        setConnectTime: function (state) {
          if (state.connectTime === -1) {
            state.connectTime = new Date()
          }
        }
      },
      getters: {
        //  getConnectTime: state => state.connectTime 동치
        getConnectTime: function (state) {
          return state.connectTime
        }
      }
    }
  }
}
