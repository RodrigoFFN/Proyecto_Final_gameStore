<template>
  <div>
    <h1>Games</h1>
    <ul>
      <li v-for="game in games" :key="game.id">
        {{ game.title }} - {{ game.price }}$
      </li>
    </ul>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import { fetchVideogames } from '../api/videogames'

export default {
  setup() {
    const games = ref([])

    onMounted(async () => {
      games.value = await fetchVideogames()
    })

    return { games }
  }
}
</script>
