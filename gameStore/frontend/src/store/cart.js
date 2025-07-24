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

})
