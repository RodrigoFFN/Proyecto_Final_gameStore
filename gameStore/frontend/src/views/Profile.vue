<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="form">
      <form @submit.prevent="updateProfile">
        <label>Email:</label>
        <input type="email" v-model="form.email" />

        <label>First Name:</label>
        <input type="text" v-model="form.first_name" />

        <label>Last Name:</label>
        <input type="text" v-model="form.last_name" />

        <label>Address:</label>
        <textarea v-model="form.address"></textarea>

        <label>Phone:</label>
        <input type="text" v-model="form.phone" />

        <button type="submit">Save Changes</button>
      </form>
    </div>

    <div v-else>
      <p>Loading user data...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/api'

const form = ref(null)

onMounted(async () => {
  try {
    const res = await api.get('api/my-profile/')
    const data = res.data
    form.value = {
      email: data.user.email || '',
      first_name: data.user.first_name || '',
      last_name: data.user.last_name || '',
      address: data.address || '',
      phone: data.phone || ''
    }
  } catch (err) {
    console.error('Error loading profile:', err)
  }
})

const updateProfile = async () => {
  try {
    const payload = {
      user: {
        email: form.value.email,
        first_name: form.value.first_name,
        last_name: form.value.last_name
      },
      address: form.value.address,
      phone: form.value.phone
    }

    await api.patch('api/my-profile/', payload)
    alert('Profile updated successfully!')
  } catch (err) {
    console.error('Update failed:', err)
    alert('Error updating profile.')
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  max-width: 400px;
}
label {
  font-weight: bold;
}
input, textarea {
  padding: 0.5rem;
  font-size: 1rem;
}
button {
  margin-top: 1rem;
  padding: 0.6rem;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #005fa3;
}
</style>
