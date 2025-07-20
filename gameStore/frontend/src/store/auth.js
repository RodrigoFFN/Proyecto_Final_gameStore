import { defineStore } from 'pinia'
import api from '../api/api'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: null,
        refreshToken: null,
        user: null,
    }),
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
        logout() {
            this.accessToken = null
            this.refreshToken = null
            this.user = null;
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
        },
    }
})