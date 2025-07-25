<template>
  <div>
    <h2>Videojuegos de categoría {{ categoryId }}</h2>
    <div v-if="games.length">
      <ul>
        <li v-for="game in games" :key="game.id">
          <router-link :to="`/game/${game.id}`">{{ game.title }}</router-link>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No hay juegos en esta categoría.</p>
    </div>
  </div>
</template>

<script>
import api from '@/api/api'

export default {
  data() {
    return {
      games: [],
      categoryId: this.$route.params.id
    }
  },
  async created() {
    const res = await api.get(`api/videogame/?category_id=${this.categoryId}`)
    this.games = res.data
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h2 {
  font-family: 'Press Start 2P', monospace;
  color: #77d9ff;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  text-shadow: 1px 1px #111;
}

div {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #e0e0e0;
  padding: 2rem;
  background-color: #2a2a2a;
  border-radius: 12px;
  max-width: 700px;
  margin: 4rem auto;
  box-shadow: 0 0 6px #77d9ff22;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 1rem;
  padding: 0.8rem 1rem;
  background-color: #202020;
  border-left: 4px solid #77d9ff;
  border-radius: 8px;
  transition: background-color 0.2s ease;
}

li:hover {
  background-color: #2f2f2f;
}

a {
  color: #77d9ff;
  text-decoration: none;
}

a:hover {
  color: #a0f0ff;
  text-shadow: 0 0 4px #77d9ff88;
}

p {
  color: #aaa;
  font-size: 0.7rem;
  margin-top: 1rem;
}
</style>

