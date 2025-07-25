<template>
  <div id="app">
    <header class="navbar">
      <h1 class="title">
        <router-link to="/" class="title-link">ESGames</router-link>
      </h1>
      <nav class="nav-links">
        <router-link to="/categories">Categories</router-link>
        <router-link v-if="!auth.isAuthenticated" to="/login">Login</router-link>
        <router-link v-if="!auth.isAuthenticated" to="/register">Register</router-link>

        <router-link v-if="auth.isAuthenticated" to="/profile">My Profile</router-link>
        <router-link v-if="auth.isAuthenticated" to="/library">My Library</router-link>
        <router-link v-if="auth.isAuthenticated" to="/cart">
          Cart<span v-if="cart.totalItems > 0"> ({{ cart.totalItems }})</span>
        </router-link>
        <button v-if="auth.isAuthenticated" class="logout-btn" @click="logout">Logout</button>
      </nav>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/store/auth.js'
import { useCartStore } from '@/store/cart.js'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const cart = useCartStore()
const router = useRouter()

auth.loadFromStorage()
if (auth.isAuthenticated) cart.fetchCartItems()

const logout = () => {
  auth.logout()
  router.push('/')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

#app {
  background-color: #1e1e1e;
  min-height: 100vh;
  color: #e0e0e0;
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2a2a2a;
  padding: 1rem 2rem;
  box-shadow: 0 0 8px #77d9ff44;
  border-bottom: 2px solid #77d9ff22;
}

.title {
  margin: 0;
  font-size: 0.9rem;
}
</style>