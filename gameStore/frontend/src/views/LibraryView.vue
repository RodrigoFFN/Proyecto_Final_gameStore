<template>
  <div>
    <h2>My Library</h2>

    <div v-if="games.length === 0">
      You haven't purchased any games yet.
    </div>
    <div v-else>
      <ul>
        <li v-for="game in games" :key="game.videogame.id">
          <strong>{{ game.videogame.title }}</strong> — {{ game.videogame.category.name }} — ${{ game.videogame.price }}
          <br />
          <small>Acquired: {{ formatDate(game.acquired_date) }}</small>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/api'

const games = ref([])

const fetchLibrary = async () => {
  try {
    const res = await api.get('api/library/')
    games.value = res.data
  } catch (err) {
    console.error('Error fetching library:', err)
  }
}

const formatDate = (isoDate) => {
  const date = new Date(isoDate)
  return date.toLocaleDateString()
}

onMounted(fetchLibrary)
</script>

<style scoped>
h2 {
  margin-bottom: 1rem;
}
li {
  margin-bottom: 1rem;
}
</style>