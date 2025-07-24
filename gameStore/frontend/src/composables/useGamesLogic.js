import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '@/store/auth'
import { useCartStore } from '@/store/cart'
import api from '@/api/api'
import { fetchVideogames } from '@/api/videogames'

export function useGamesLogic() {
    const auth = useAuthStore()
    const cart = useCartStore()
    const isAuthenticated = computed(() => !!auth.accessToken)
    const cartItems = computed(() => cart.cartItems)

    const videogames = ref([])
    const loading = ref(true)
    const categories = ref([])
    const selectedCategory = ref(null)
    const favorites = ref([])
    const purchasedGames = ref([])

    const loadGames = async () => {
        try {
            videogames.value = await fetchVideogames()
        } catch (err) {
            console.error('Error fetching games:', err)
        } finally {
            loading.value = false
        }
    }
}