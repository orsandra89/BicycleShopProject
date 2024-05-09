<template>
  <v-app>
    <AppNavbar />
    <HelloWorld msg="App" />
  </v-app>
</template>

<script>
import AppNavbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    AppNavbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>