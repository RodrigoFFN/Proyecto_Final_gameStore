<template>
  <div>
    <h1>Categorías</h1>
    <ul>
      <li v-for="cat in categories" :key="cat.id">
        <router-link :to="`/category/${cat.id}`">{{ cat.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import api from '@/api/api'

export default {
  data() {
    return {
      categories: []
    }
  },
  async created() {
    const res = await api.get('api/category/')
    this.categories = res.data
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h1 {
  font-family: 'Press Start 2P', monospace;
  color: #77d9ff;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  text-shadow: 1px 1px #111;
  text-align: center;
}

div {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #e0e0e0;
  padding: 2rem;
  background-color: #2a2a2a;
  border-radius: 12px;
  max-width: 600px;
  margin: 4rem auto;
  box-shadow: 0 0 6px #77d9ff22;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
}

li {
  margin-bottom: 1rem;
  padding: 0.8rem 1rem;
  background-color: #202020;
  border-left: 4px solid #77d9ff;
  border-radius: 8px;
  box-shadow: 0 0 5px #77d9ff22;
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
</style>
