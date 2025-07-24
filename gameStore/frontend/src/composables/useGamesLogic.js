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

    const loadCategories = async () => {
        try {
            const res = await api.get('api/category/')
            categories.value = res.data
        } catch (err) {
            console.error('Error loading categories:', err)
        }
    }

    const fetchFavorites = async () => {
        if (!isAuthenticated.value) return
        try {
            const res = await api.get('api/favorites/')
            favorites.value = res.data
        } catch (err) {
            console.error('Error fetching favorites:', err)
        }
    }

    const fetchPurchasedGames = async () => {
        if (!isAuthenticated.value) return
        try {
            const res = await api.get('api/library/')
            purchasedGames.value = res.data
        } catch (err) {
            console.error('Error fetching purchased games:', err)
        }
    }

    const filteredGames = computed(() => {
        if (!selectedCategory.value) return videogames.value
        return videogames.value.filter(game =>
            game.category && game.category.id === selectedCategory.value
        )
    })
}