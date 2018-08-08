// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/*
  mixin은 적용하려는 대상의 각 컴포넌트에 모두 적용되기에
  새로 갱신이 일어나는 컴포넌트가 있을 경우 mixin에서 data를 쓰면 위험하다.
*/
Vue.mixin({
  methods: {
    echoMixin (text = 'hello world') {
      console.log(text)
      return text
    },
    getCurrentTime () {
      return new Date()
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
