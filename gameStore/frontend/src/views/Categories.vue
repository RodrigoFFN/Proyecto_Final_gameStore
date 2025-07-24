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