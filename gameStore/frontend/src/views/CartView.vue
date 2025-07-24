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