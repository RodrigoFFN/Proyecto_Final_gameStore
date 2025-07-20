import api from './api'

export async function fetchVideogames() {
    const response = await api.get('/api/videogame/')
    return response.data
}