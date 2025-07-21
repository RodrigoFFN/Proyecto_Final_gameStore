<template>
  <div id="app">
    <header>
      <h1>GameStore</h1>
      <nav>
        <router-link v-if="!auth.isAuthenticated" to="/login">Login</router-link>
        <router-link v-if="!auth.isAuthenticated" to="/register">Register</router-link>
        <router-link v-if="auth.isAuthenticated" to="/profile">My Profile</router-link>
        <button v-if="auth.isAuthenticated" @click="logout">Logout</button>
      </nav>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/store/auth.js'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

auth.loadFromStorage()

const logout = () => {
  auth.logout()
  router.push('/')
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

nav {
  margin-top: 0.5rem;
}

nav a,
nav button {
  margin: 0 0.5rem;
  color: white;
  text-decoration: none;
  background: none;
  border: none;
  cursor: pointer;
  font-weight: bold;
}

nav button:hover,
nav a:hover {
  text-decoration: underline;
}

main {
  margin-top: 2rem;
}
</style>