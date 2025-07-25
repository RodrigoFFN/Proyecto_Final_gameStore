<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="user && profile">
        <div class="profile-info">
    <p><span>👤 Username:</span> {{ user.username }}</p>
    <p><span>📧 Email:</span> {{ user.email }}</p>
    <p v-if="profile.address"><span>🏠 Address:</span> {{ profile.address }}</p>
    <p v-if="profile.phone"><span>📞 Phone:</span> {{ profile.phone }}</p>
    <p><span>💰 Saldo:</span> ${{ profile.balance }}</p>
  </div>

      <div style="margin-top: 20px;">
        <h3>Recharge Balance</h3>
        <input
          type="number"
          v-model.number="rechargeAmount"
          placeholder="Amount to add"
          min="1"
        />
        <button @click="rechargeBalance" :disabled="!validAmount">Add</button>

        <p v-if="successMessage" style="color: green;">{{ successMessage }}</p>
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
      </div>
      <h2></h2>
      <h2></h2>
      <h2>🎮 Mis Favoritos</h2>
      <ul v-if="favorites.length > 0">
        <li v-for="fav in favorites" :key="fav.id">
          <router-link :to="`/game/${fav.videogame}`">{{ fav.videogame_title }}</router-link>
          <span v-if="fav.videogame_price"> - ${{ fav.videogame_price }}</span>
          <button @click="removeFavorite(fav.id)" class="remove-fav">❌ Quitar</button>
        </li>
      </ul>
      <p v-else>No tienes juegos en favoritos aún.</p>
    </div>
    <div v-else>
      <p>Loading user data...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '@/api/api'

const user = ref(null)
const profile = ref(null)
const rechargeAmount = ref(null)
const favorites = ref([])
const successMessage = ref('')
const errorMessage = ref('')

const validAmount = computed(() => {
  return rechargeAmount.value && rechargeAmount.value > 0
})

const loadProfile = async () => {
  try {
    const res = await api.get('api/my-profile/')
    user.value = res.data.user
    profile.value = {
      address: res.data.address,
      phone: res.data.phone,
      balance: res.data.balance
    }
  } catch (err) {
    console.error('Error loading profile:', err)
  }
}

const rechargeBalance = async () => {
  successMessage.value = ''
  errorMessage.value = ''

  if (!validAmount.value) {
    errorMessage.value = 'Please enter a valid amount greater than 0.'
    return
  }

  try {
    await api.post('api/recharge/', {
      amount: rechargeAmount.value
    })
    rechargeAmount.value = null
    successMessage.value = 'Balance updated successfully.'
    await loadProfile()
  } catch (err) {
    errorMessage.value = 'There was an error while recharging.'
    console.error('Error recharging balance:', err)
  }
}

const fetchFavorites = async () => {
  try {
    const res = await api.get('api/favorites/')
    favorites.value = res.data
  } catch (err) {
    console.error('Error al cargar favoritos:', err)
  }
}

const removeFavorite = async (favoriteId) => {
  try {
    await api.delete(`api/favorites/${favoriteId}/`)
    favorites.value = favorites.value.filter(fav => fav.id !== favoriteId)
    alert('El juego fue quitado de favoritos')
  } catch (err) {
    console.error('Error al quitar favorito:', err)
  }
}


onMounted(() => {
  loadProfile()
  fetchFavorites()  
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h2 {
  font-family: 'Press Start 2P', monospace;
  color: #44f2ff;
  text-shadow: 1px 1px #000;
  margin-bottom: 1rem;
  font-size: 1rem;
}

h3 {
  font-family: 'Press Start 2P', monospace;
  color: #ff5a7d;
  font-size: 0.9rem;
  margin: 1.5rem 0 1rem;
}

p {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #000000ff;
  margin-bottom: 0.5rem;
}

input {
  padding: 0.5rem;
  font-size: 0.7rem;
  border-radius: 6px;
  border: 1px solid #44f2ff;
  background-color: #1f1f1f;
  color: #cfffff;
  font-family: 'Press Start 2P', monospace;
  outline: none;
  margin-right: 0.5rem;
}

button {
  padding: 0.5rem 1rem;
  font-size: 0.7rem;
  border: none;
  border-radius: 6px;
  background-color: #ff3366;
  color: white;
  font-family: 'Press Start 2P', monospace;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

button:hover {
  background-color: #ff5a7d;
  box-shadow: 0 0 8px #ff336688;
}

.remove-fav {
  margin-left: 0.5rem;
  background-color: transparent;
  color: #ff4444;
  border: 1px solid #ff4444;
}

.remove-fav:hover {
  background-color: #ff4444;
  color: white;
}

ul {
  list-style: none;
  padding-left: 0;
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #cfffff;
}

a {
  color: #44f2ff;
  text-decoration: none;
}

a:hover {
  color: #88ffff;
  text-shadow: 0 0 4px #44f2ff;
}

.success-message {
  color: #66ffcc;
  font-size: 0.7rem;
  margin-top: 0.5rem;
}

.error-message {
  color: #ff7777;
  font-size: 0.7rem;
  margin-top: 0.5rem;
}

.profile-card {
  background-color: #222;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 0 15px #44f2ff33;
  margin-bottom: 2rem;
}

.profile-info p {
  margin: 0.5rem 0;
  font-size: 0.75rem;
  color: #e0f7fa;
}

.profile-info span {
  color: #44f2ff;
  font-weight: bold;
}

.profile-card input {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  width: 150px;
}

.profile-card button {
  margin-top: 0.5rem;
}

</style>
