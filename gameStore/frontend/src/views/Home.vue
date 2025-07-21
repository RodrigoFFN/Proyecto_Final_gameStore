<template>
  <div>
    <h1>Welcome to GameStore!</h1>

    <div v-if="isAuthenticated">
      <p>Welcome back, {{ userName }}!</p>
      <button @click="goToCart">Go to Cart</button>
      <button @click="goToProfile">Profile</button>
    </div>

    <h2>Available Videogames</h2>
    <div v-if="loading">Loading games...</div>
    <div v-else-if="videogames.length === 0">No games found.</div>

    <div v-else class="games-list">
      <div v-for="game in videogames" :key="game.id" class="game-card">
        <img
          v-if="game.image_url"
          :src="game.image_url"
          alt="Game cover"
          class="game-image"
        />
        <h3>{{ game.title }}</h3>
        <p>{{ game.description }}</p>
        <p><strong>Price:</strong> ${{ game.price }}</p>
        <p v-if="game.category"><strong>Category:</strong> {{ game.category.name }}</p>
        <p v-if="game.release_date"><strong>Release Date:</strong> {{ formatDate(game.release_date) }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'
import { fetchVideogames } from '../api/videogames'

const router = useRouter()
const auth = useAuthStore()

const isAuthenticated = computed(() => !!auth.accessToken)
const userName = computed(() => auth.user?.username || '')

const videogames = ref([])
const loading = ref(true)

const loadGames = async () => {
  try {
    videogames.value = await fetchVideogames()
  } catch (error) {
    console.error("Error fetching games:", error)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString()
}

onMounted(loadGames)

const goToCart = () => router.push('/cart')
const goToProfile = () => router.push('/profile')
</script>

<style scoped>
.games-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.game-card {
  border: 1px solid #ccc;
  padding: 1rem;
  width: 250px;
  border-radius: 8px;
}

.game-image {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}
</style>
