import axios from 'axios'
import { useAuthStore } from '../store/auth'

const api = axios.create({
    baseURL: 'https://gamestore-backend-g1xi.onrender.com/',
    headers: {
        'Content-Type': 'application/json',
    }
})

api.interceptors.request.use(config => {
    const auth = useAuthStore()
    if (auth.accessToken) {
        config.headers.Authorization = `Bearer ${auth.accessToken}`
    }
    return config
})

export default api