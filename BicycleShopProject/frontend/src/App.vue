<template>
  <div id="app" class="d-flex flex-column min-vh-100">
    <AppNavbar />
    <router-view class="flex-grow-1" />
    <Stopka />
  </div>
</template>

<script>
import AppNavbar from './components/Navbar.vue'
import Stopka from './components/Stopka.vue'

export default {
  name: 'App',
  components: {
    AppNavbar,
    Stopka
  }
}
</script>

<style></style>