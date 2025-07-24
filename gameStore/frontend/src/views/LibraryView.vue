<template>
  <div>
    <h2>My Library</h2>

    <div v-if="games.length === 0">
      You haven't purchased any games yet.
    </div>
    <div v-else>
      <ul>
        <li v-for="game in games" :key="game.videogame.id">
          <strong>{{ game.videogame.title }}</strong> — {{ game.videogame.category.name }} — ${{ game.videogame.price }}
          <br />
          <small>Acquired: {{ formatDate(game.acquired_date) }}</small>
        </li>
      </ul>
    </div>
  </div>
</template>