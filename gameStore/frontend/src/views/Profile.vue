<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="user && profile">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p v-if="profile.address"><strong>Address:</strong> {{ profile.address }}</p>
      <p v-if="profile.phone"><strong>Phone:</strong> {{ profile.phone }}</p>
    </div>

    <div v-else>
      <p>Loading user data...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/api'

const user = ref(null)
const profile = ref(null)

onMounted(async () => {
  try {
    const res = await api.get('api/my-profile/')
    user.value = res.data.user
    profile.value = {
      address: res.data.address,
      phone: res.data.phone
    }
  } catch (err) {
    console.error('Error loading profile:', err)
  }
})
</script>

<style scoped>
h2 {
  margin-bottom: 1rem;
}
p {
  margin: 0.5rem 0;
}
</style>
