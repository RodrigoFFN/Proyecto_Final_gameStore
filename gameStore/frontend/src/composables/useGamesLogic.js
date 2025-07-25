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

    const isInCart = (gameId) => {
        return cartItems.value.some(item => item.videogame?.id === gameId)
    }

    const isPurchased = (gameId) => {
        return purchasedGames.value.some(item => item.videogame?.id === gameId)
    }

    const isFavorite = (gameId) => {
        return favorites.value.some(fav =>
            typeof fav.videogame === 'number' ? fav.videogame === gameId : fav.videogame?.id === gameId)
    }

    const toggleFavorite = async (game) => {
        if (!isFavorite(game.id)) {
            try {
                const res = await api.post('api/favorites/', {
                    videogame: game.id
                })
                favorites.value.push(res.data)
                alert('Agregado a favoritos')
            } catch (err) {
                console.error('Error agregando favorito:', err)
            }
        } else {
            try {
                const fav = favorites.value.find(fav => fav.videogame === game.id)
                await api.delete(`api/favorites/${fav.id}/`)
                favorites.value = favorites.value.filter(f => f.id !== fav.id)
                alert('Quitado de favoritos')
            } catch (err) {
                console.error('Error quitando favorito:', err)
            }
        }
    }

    const addToCart = async (gameId) => {
        try {
            await cart.addToCart(gameId)
            alert("Game added to cart!")
        } catch (err) {
            console.error('Error adding to cart:', err)
        }
    }

    const formatDate = (dateStr) => {
        const date = new Date(dateStr)
        return date.toLocaleDateString()
    }

    onMounted(() => {
        loadGames()
        loadCategories()
        fetchFavorites()
        fetchPurchasedGames()
        if (isAuthenticated.value) {
            cart.fetchCartItems()
        }
    })

    return {
        videogames,
        filteredGames,
        selectedCategory,
        categories,
        addToCart,
        isInCart,
        isPurchased,
        isFavorite,
        toggleFavorite,
        fetchFavorites,
        fetchPurchasedGames,
        formatDate,
        loading
    }
}