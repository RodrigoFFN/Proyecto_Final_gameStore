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
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #222;
  color: #fff;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.title {
  margin: 0;
  font-size: 1.5rem;
}

.title-link {
  text-decoration: none;
  color: #fff;
}

.nav-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
}

.nav-links a:hover {
  text-decoration: underline;
}

.logout-btn {
  background: transparent;
  border: 1px solid #fff;
  color: #fff;
  padding: 0.3rem 0.7rem;
  border-radius: 4px;
  cursor: pointer;
}

.logout-btn:hover {
  background-color: #fff;
  color: #222;
}
</style>