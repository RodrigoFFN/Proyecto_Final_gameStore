import { defineStore } from 'pinia'
import api from '@/api/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('access') || null,
    refreshToken: localStorage.getItem('refresh') || null,
    userProfile: null
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

        localStorage.setItem('access', this.accessToken)
        localStorage.setItem('refresh', this.refreshToken)

        api.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`

        const profileRes = await api.get('api/my-profile/')
        this.userProfile = profileRes.data

        return true
      } catch (err) {
        console.error('Login failed', err)
        return false
      }
    },

    async loadFromStorage() {
      const access = localStorage.getItem('access')
      const refresh = localStorage.getItem('refresh')

      if (access) {
        this.accessToken = access
        this.refreshToken = refresh
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`

        try {
          const profileRes = await api.get('api/my-profile/')
          this.userProfile = profileRes.data
        } catch (err) {
          console.error('Failed to load user profile:', err)
          this.logout()
        }
      }
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.userProfile = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      delete api.defaults.headers.common['Authorization']
    },

    handleLoginTokens({ access, refresh }) {
      this.accessToken = access
      this.refreshToken = refresh
      localStorage.setItem('access', access)
      localStorage.setItem('refresh', refresh)
    },
    
    async fetchUserProfile() {
      try {
        const res = await api.get('api/my-profile/')
        this.userProfile = res.data
      } catch (err) {
      console.error('Failed to fetch user profile:', err)
      }
    }
  }
})
