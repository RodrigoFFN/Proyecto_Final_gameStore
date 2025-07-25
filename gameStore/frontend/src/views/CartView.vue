<template>
  <div>
    <h2>Your Cart</h2>

    <div v-if="items.length === 0">
      Your cart is empty.
    </div>
    <div v-else>
      <div v-for="item in items" :key="item.id">
        <p>
          {{ item.videogame.title }} - ${{ item.videogame.price }} x {{ item.quantity }}
        </p>
        <button @click="removeItem(item.id)">Remove</button>
      </div>

      <p><strong>Total:</strong> ${{ total }}</p>

      <button @click="checkout" :disabled="items.length === 0">Buy</button>

      <p v-if="successMessage" style="color: green;">{{ successMessage }}</p>
      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '@/api/api'

const items = ref([])
const successMessage = ref('')
const errorMessage = ref('')

const fetchCartItems = async () => {
  try {
    const res = await api.get('api/cartitem/')
    items.value = res.data
  } catch (err) {
    console.error('Error loading cart items:', err)
  }
}

const removeItem = async (id) => {
  try {
    await api.delete(`api/cartitem/${id}/`)
    fetchCartItems()
  } catch (err) {
    console.error('Error deleting item:', err)
  }
}

const checkout = async () => {
  successMessage.value = ''
  errorMessage.value = ''

  try {
    const res = await api.post('api/checkout/', {}, {
      responseType: 'blob'
    })

    const blob = new Blob([res.data], { type: 'application/pdf' })
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', 'boleta_compra.pdf')
    document.body.appendChild(link)
    link.click()
    link.remove()

    fetchCartItems()
    successMessage.value = 'Compra exitosa. Se descargó tu boleta.'

  } catch (err) {
    errorMessage.value = err.response?.data?.error || 'Checkout failed.'
    console.error('Error during checkout:', err)
  }
}

const total = computed(() =>
  items.value.reduce((sum, item) => sum + item.videogame.price * item.quantity, 0)
)

onMounted(fetchCartItems)
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h2 {
  font-family: 'Press Start 2P', monospace;
  color: #77d9ff;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  text-align: center;
  text-shadow: 1px 1px #111;
}

div {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #e0e0e0;
  background-color: #2a2a2a;
  border-radius: 12px;
  padding: 2rem;
  max-width: 700px;
  margin: 4rem auto;
  box-shadow: 0 0 6px #77d9ff22;
}

p {
  margin: 0.8rem 0;
}

strong {
  color: #ffaec9;
}

button {
  font-family: inherit;
  font-size: 0.7rem;
  background-color: #3a3a3a;
  color: #e0e0e0;
  border: 1px solid #77d9ff;
  padding: 0.5rem 1rem;
  margin-top: 0.5rem;
  margin-right: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #444;
  color: #a0f0ff;
}

button:disabled {
  background-color: #555;
  color: #999;
  cursor: not-allowed;
}

.success-message {
  color: #a4f9c8;
  margin-top: 1rem;
}

.error-message {
  color: #ff8a8a;
  margin-top: 1rem;
}
</style>
