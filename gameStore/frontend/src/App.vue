<template>
  <div id="app">
    <header>
      <h1>GameStore</h1>
      <!-- Puedes agregar navegación aquí si quieres -->
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
}
header {
  background-color: #222;
  color: white;
  padding: 1rem;
  text-align: center;
}
main {
  margin-top: 2rem;
}
</style>
