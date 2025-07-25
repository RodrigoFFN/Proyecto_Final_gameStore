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
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h2 {
  font-family: 'Press Start 2P', monospace;
  color: #44f2ff;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  text-shadow: 1px 1px #000;
}

div {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #000000ff;
  padding: 2rem;
  background-color: #5b5b5bff;
  border-radius: 12px;
  max-width: 700px;
  margin: 4rem auto;
  box-shadow: 0 0 10px #6ff5ff81;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background-color: #1f1f1f;
  border-left: 4px solid #44f2ff;
  border-radius: 8px;
  box-shadow: 0 0 6px #44f2ff22;
}

strong {
  color: #ff5a7d;
}

small {
  font-size: 0.6rem;
  color: #2d2c2cff;
  display: block;
  margin-top: 0.3rem;
}
</style>