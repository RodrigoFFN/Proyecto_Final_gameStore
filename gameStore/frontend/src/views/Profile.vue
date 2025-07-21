<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="user">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p v-if="user.first_name"><strong>First Name:</strong> {{ user.first_name }}</p>
      <p v-if="user.last_name"><strong>Last Name:</strong> {{ user.last_name }}</p>
    </div>

    <div v-else>
      <p>Loading user data...</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/store/auth'

const auth = useAuthStore()
const user = computed(() => auth.user)
</script>

<style scoped>
h2 {
  margin-bottom: 1rem;
}
p {
  margin: 0.5rem 0;
}
</style>
