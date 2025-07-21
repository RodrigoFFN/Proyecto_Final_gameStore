import { defineStore } from 'pinia'
import api from '@/api/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('access') || null,
    refreshToken: localStorage.getItem('refresh') || null,
    user: null
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.accessToken
  },
  
  actions: {
    async login(username, password) {
      try {
        const res = await api.post('api/token/', { username, password })
        this.accessToken = res.data.access
        this.refreshToken = res.data.refresh
        this.user = { username }
        localStorage.setItem('access', this.accessToken)
        localStorage.setItem('refresh', this.refreshToken)
        return true
      } catch (err) {
        console.error('Login failed', err)
        return false
      }
    },

    handleLoginTokens({ access, refresh, username }) {
      this.accessToken = access
      this.refreshToken = refresh
      this.user = { username }

      localStorage.setItem('access', access)
      localStorage.setItem('refresh', refresh)
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
    },

    loadFromStorage() {
      const access = localStorage.getItem('access')
      const refresh = localStorage.getItem('refresh')
      if (access) {
        this.accessToken = access
        this.refreshToken = refresh
        this.user = { username: 'usuario' }
      }
    }
  }
})