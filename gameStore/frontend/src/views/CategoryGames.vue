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
