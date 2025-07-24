import { defineStore } from 'pinia'
import api from '@/api/api'

export const useCartStore = defineStore('cart', {
  state: () => ({
    cartItems: [],
  }),

})
