<template>
  <div v-if="game">
    <h1>
      {{ game.title }}
      <span v-if="averageRating !== null" style="font-size: 18px; margin-left: 10px;">
        ({{ averageRating.toFixed(1) }} ★)
      </span>
    </h1>

    <img :src="game.image_url" alt="Game Image" style="max-width: 300px;" />
    <p>{{ game.description }}</p>
    <p><strong>Price:</strong> ${{ game.price }}</p>
    <p><strong>Category:</strong> {{ game.category?.name || 'Uncategorized' }}</p>
    <p><strong>Release Date:</strong> {{ game.release_date }}</p>

    <hr />

    <h2>Reviews</h2>
    <div v-if="reviews.length === 0">No reviews yet.</div>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        <strong>{{ review.user.user.username }}</strong>:
        <template v-if="editingId === review.id">
          <input v-model="editText" style="width: 70%;" />
          <select v-model="editRating">
            <option disabled value="">Select rating</option>
            <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
          </select>
          <button @click="updateReview(review.id)">Save</button>
          <button @click="cancelEdit">Cancel</button>
        </template>
        <template v-else>
          {{ review.comment }}<br />
          <strong>Rating:</strong>
          {{ '★'.repeat(review.rating) + '☆'.repeat(5 - review.rating) }}<br />
          <small>{{ new Date(review.date).toLocaleDateString() }}</small>

          <template v-if="review.user.user.id === auth.user.id">
            <button @click="startEdit(review)">Edit</button>
            <button @click="deleteReview(review.id)">Delete</button>
          </template>
        </template>
      </li>
    </ul>

    <div v-if="isAuthenticated" style="margin-top: 20px;">
      <textarea
        v-model="newReview"
        placeholder="Write your review..."
        rows="3"
        style="width: 100%;"
      ></textarea>
      <br />
      <select v-model="newRating">
        <option disabled value="">Select rating</option>
        <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
      </select>
      <button @click="submitReview" :disabled="!newReview.trim() || !newRating">Submit</button>
    </div>
    <div v-else>
      <p><em>You must be logged in to write a review.</em></p>
    </div>
  </div>

  <div v-else>
    <p>Loading game details...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api/api'
import { useAuthStore } from '@/store/auth'

const route = useRoute()
const auth = useAuthStore()
const gameId = route.params.id

const game = ref(null)
const reviews = ref([])
const newReview = ref('')
const newRating = ref('')
const averageRating = ref(null)

const editingId = ref(null)
const editText = ref('')
const editRating = ref('')

const isAuthenticated = computed(() => auth.accessToken !== null)

const fetchGame = async () => {
  try {
    const res = await api.get(`api/videogame/${gameId}/`)
    game.value = res.data
  } catch (err) {
    console.error('Error loading game:', err)
  }
}

const fetchReviews = async () => {
  try {
    const res = await api.get('api/review/', {
      params: { videogame: gameId }
    })
    reviews.value = res.data
    calculateAverageRating()
  } catch (err) {
    console.error('Error loading reviews:', err)
  }
}

const calculateAverageRating = () => {
  if (reviews.value.length === 0) {
    averageRating.value = null
    return
  }
  const total = reviews.value.reduce((sum, r) => sum + r.rating, 0)
  averageRating.value = total / reviews.value.length
}

const submitReview = async () => {
  try {
    await api.post('api/review/', {
      comment: newReview.value,
      rating: newRating.value,
      videogame_id: gameId
    })
    newReview.value = ''
    newRating.value = ''
    await fetchReviews()
  } catch (err) {
    console.error('Error submitting review:', err)
  }
}

const startEdit = (review) => {
  editingId.value = review.id
  editText.value = review.comment
  editRating.value = review.rating
}

const cancelEdit = () => {
  editingId.value = null
  editText.value = ''
  editRating.value = ''
}

const updateReview = async (reviewId) => {
  try {
    await api.put(`api/review/${reviewId}/`, {
      comment: editText.value,
      rating: editRating.value,
      videogame_id: gameId
    })
    editingId.value = null
    editText.value = ''
    editRating.value = ''
    await fetchReviews()
  } catch (err) {
    console.error('Error updating review:', err)
  }
}

const deleteReview = async (reviewId) => {
  if (!confirm('Are you sure you want to delete this review?')) return
  try {
    await api.delete(`api/review/${reviewId}/`)
    await fetchReviews()
  } catch (err) {
    console.error('Error deleting review:', err)
  }
}

onMounted(() => {
  fetchGame()
  fetchReviews()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

h1 {
  font-family: 'Press Start 2P', monospace;
  color: #44f2ff;
  font-size: 1rem;
  margin-bottom: 1rem;
  text-shadow: 1px 1px #000;
}

h2 {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.9rem;
  color: #ff5a7d;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

p {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.7rem;
  color: #e0e0e0;
  margin: 0.5rem 0;
}

img {
  border-radius: 8px;
  box-shadow: 0 0 10px #44f2ff55;
  margin-bottom: 1rem;
}

textarea,
input,
select {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.65rem;
  padding: 0.5rem;
  border-radius: 6px;
  border: 1px solid #44f2ff;
  background-color: #1f1f1f;
  color: #cfffff;
  margin: 0.3rem 0;
  width: 100%;
  box-sizing: border-box;
}

button {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.65rem;
  padding: 0.4rem 0.8rem;
  border: none;
  border-radius: 6px;
  background-color: #ff3366;
  color: white;
  cursor: pointer;
  margin-top: 0.5rem;
  transition: all 0.3s ease-in-out;
  margin-right: 0.3rem;
}

button:hover {
  background-color: #ff5a7d;
  box-shadow: 0 0 8px #ff336688;
}
</style>
