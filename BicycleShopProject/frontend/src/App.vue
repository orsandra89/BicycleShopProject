<template>
  <div id="app">
    <AppNavbar />
    <Main />
    <Stopka />
  </div>
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

<style></style>