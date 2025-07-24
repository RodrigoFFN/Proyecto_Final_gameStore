import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '@/store/auth'
import { useCartStore } from '@/store/cart'
import api from '@/api/api'
import { fetchVideogames } from '@/api/videogames'

export function useGamesLogic() {
}