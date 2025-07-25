<template>
  <div id="app">
    <header class="navbar">
      <h1 class="title">
        <router-link to="/" class="title-link">ESGames</router-link>
      </h1>
      <nav class="nav-links">
        <router-link to="/categories">Categories</router-link>
        <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
        <router-link v-if="!isAuthenticated" to="/register">Register</router-link>

        <router-link v-if="isAuthenticated" to="/profile">My Profile</router-link>
        <router-link v-if="isAuthenticated" to="/library">My Library</router-link>
        <router-link v-if="isAuthenticated" to="/cart">
          Cart<span v-if="cart.totalItems > 0"> ({{ cart.totalItems }})</span>
        </router-link>
        <span v-if="isAuthenticated" class="balance">
          Balance: ${{ userBalance }}
        </span>
        <button v-if="isAuthenticated" class="logout-btn" @click="logout">Logout</button>
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
import { computed, onMounted } from 'vue'

const auth = useAuthStore()
const cart = useCartStore()
const router = useRouter()

const isAuthenticated = computed(() => auth.isAuthenticated)
const userBalance = computed(() => auth.userProfile?.balance || 0)

onMounted(async () => {
  await auth.loadFromStorage()
  if (auth.isAuthenticated) {
    await cart.fetchCartItems()
  }
})

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

.title-link {
  color: #77d9ff;
  text-decoration: none;
  text-shadow: 1px 1px #111;
}

.title-link:hover {
  color: #a0f0ff;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

.nav-links a {
  color: #ffffffcc;
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: #77d9ff;
  text-shadow: 0 0 5px #77d9ff88;
}

.balance {
  color: #00ff00;
  font-weight: bold;
  margin-left: 1rem;
}

.logout-btn {
  background-color: transparent;
  color: #ff8a8a;
  border: 1px solid #ff8a8a88;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-family: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.logout-btn:hover {
  background-color: #ff8a8a22;
  color: #ffffff;
}

main {
  padding: 2rem;
}
</style>