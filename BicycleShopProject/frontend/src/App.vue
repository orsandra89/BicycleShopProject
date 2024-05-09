<template>
  <v-app>
    <AppNavbar />
    <Main />
    <Stopka />
  </v-app>
</template>

<script>
import AppNavbar from './components/Navbar.vue'
import Stopka from './components/Stopka.vue'
import Main from './components/Main.vue'

export default {
  name: 'App',
  components: {
    AppNavbar,
    Main,
    Stopka
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