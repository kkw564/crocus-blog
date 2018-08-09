<template>
  <div id="app">
    <div id="mainpage" v-show="!isMain" >
      <div id="particles-js" v-show="!isMain" >
          <div class='console-container' v-show="!isMain" @click="goBlog">
              <span id='text' v-show="!isMain"></span>
              <div class='console-underscore' id='console' v-show="!isMain">_
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { consoleText } from '../static/js/mainpage.js'

export default {
  name: 'App',
  data () {
    return {
      isMain: false,
      crocus: 'http://www.crocus.co.kr',
      a: '',
      b: ''
    }
  },
  created: function () {
    this.$store.commit('crocus/setConnectTime')
    console.log('Welcome to Crocus')
    let connectTime = this.$store.getters['crocus/getConnectTime']
    console.log('Your connect time is %s', connectTime)
  },
  mounted: function () {
    this.isMain = false
    particlesJS.load('particles-js', '../static/json/particlesjs-config.json', function () {

    })
    consoleText(['Think Creatively', 'Solve Flexibly', 'Advance Yourself', 'Have a Dream', 'With Crocus'], 'text', ['white'])
    // if (document.location.href === this.crocus) {
    //   this.isMain = false
    // } else {
    //   this.isMain = true
    // }
  },

  methods: {
    goBlog: function () {
      this.isMain = true
      // this.mixinTest()
    },
    mixinTest: function () {
      this.echoMixin()
      this.echoMixin('bye')
      console.log(this.a = this.getCurrentTime())
      for (var i = 0; i < 2000000000; i++) {}
      console.log(this.b = this.getCurrentTime())
      console.log((this.b.getTime() - this.a.getTime()) / 1000)
    }
  }
}
</script>

<style>
  /* ---- reset ---- */
  body{
      margin:0;
      font:normal 75% Arial, Helvetica, sans-serif;
  }
  canvas{
      display: block;
      vertical-align: bottom;
  }
  /* ---- particles.js container ---- */
  #particles-js{
      position:absolute;
      width: 100%;
      height: 100%;
      background-color: transparent;
      background-image: url("./assets/image/starry.jpg");
      background-repeat: no-repeat;
      background-size: cover;
      background-position: 50% 50%;
  }
  .console-container{
      font-size: 35px;
      color:white;
      user-select: none;
      position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)
  }
  .hidden {
      opacity:0;
  }
  .console-underscore {
      display:inline-block;
      color:tomato;
      position:relative;
      top:-0.14em;
      left:-8px;
  }
  .full-page{
      width:100%;
      height:100%;
      display:absolute;
  }
</style>
