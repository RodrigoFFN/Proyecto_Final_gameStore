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

  </div>

</template>
