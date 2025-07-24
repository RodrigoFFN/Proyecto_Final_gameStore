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


</template>
