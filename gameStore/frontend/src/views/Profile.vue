<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="user && profile">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p v-if="profile.address"><strong>Address:</strong> {{ profile.address }}</p>
      <p v-if="profile.phone"><strong>Phone:</strong> {{ profile.phone }}</p>
      <p><strong>Balance:</strong> ${{ profile.balance }}</p>

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
