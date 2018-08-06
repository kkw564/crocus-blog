<template>
  <div id="app">
    <div> {{ vueTest }} </div>
    <div> {{ crocus }} </div>
  </div>
</template>

<script>
export default {
  name: 'App',

  data () {
    return {
      vueTest: 'hello world',
      crocus: 'www.crocus.co.kr'
    }
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
