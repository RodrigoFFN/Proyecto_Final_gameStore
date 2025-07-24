import { defineStore } from 'pinia'
import api from '@/api/api'

export const useCartStore = defineStore('cart', {
  state: () => ({
    cartItems: [],
  }),
  getters: {
    totalItems: (state) =>
      state.cartItems.reduce((sum, item) => sum + item.quantity, 0),
  },
  actions: {
    async fetchCartItems() {
      try {
        const res = await api.get('api/cartitem/')
        this.cartItems = res.data
      } catch (error) {
        console.error('Error al obtener ítems del carrito:', error)
      }
    },

  },
})
