<template>
  <div>
    <h1>Welcome to GameStore!</h1>

    <div v-if="!isAuthenticated">
      <p>Welcome back, {{ userName }}!</p>
      <button @click="goToCart">Go to Cart</button>
      <button @click="goToProfile">Profile</button>
    </div>

    <!-- Aquí iría tu lista de videojuegos -->
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

const router = useRouter()
const auth = useAuthStore()

const isAuthenticated = computed(() => !!auth.accessToken)
const userName = computed(() => auth.user?.username || '')

const goToLogin = () => router.push('/login')
const goToRegister = () => router.push('/register')
const goToCart = () => router.push('/cart')
const goToProfile = () => router.push('/profile')
</script>
