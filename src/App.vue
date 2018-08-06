<template>
  <div id="app">
    <div> {{ vueTest }} </div>
    <div> {{ crocus }} </div>
    <div> {{ branch2 }} </div>
    <div> {{ branch3 }} </div>
    <div v-if="rebase == 2"> this is rebase2 </div>
    <div v-if="rebase == 3"> this is rebase3 </div>
  </div>
</template>

<script>
export default {
  name: 'App',

  data () {
    return {
      vueTest: 'hello world',
      crocus: 'www.crocus.co.kr',
      branch2: 'This is branch2',
      branch3: 'now branch is branch3',
      rebase: 0
    }
  },

  created () {
    var d = new Date()
    this.rebase = (d % 2) + 2
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
