<template>
  <b-container class="py-4">
    <b-row>
      <b-col>
        <h1 class="display-4 text-primary mb-4">🎮 Bienvenido a ESGames</h1>
        <div v-if="isAuthenticated" class="mb-3 h5">
          ¡Hola de nuevo, <span class="text-danger fw-semibold">{{ userName }}</span>!
        </div>
      </b-col>
    </b-row>

    <b-row class="mb-4">
      <b-col md="6">
        <b-form-group label="Filtrar por categoría" label-for="category-select">
          <b-form-select
            id="category-select"
            v-model="selectedCategory"
            :options="categoryOptions"
            class="mb-3"
          ></b-form-select>
        </b-form-group>
      </b-col>
    </b-row>

    <b-row>
      <b-col>
        <h2 class="h4 mb-3">🎲 Juegos disponibles</h2>
        <div v-if="loading" class="text-warning">Cargando videojuegos...</div>
        <div v-else-if="filteredGames.length === 0" class="text-danger">No se encontraron videojuegos.</div>
      </b-col>
    </b-row>

    <b-row>
      <b-col
        v-for="game in filteredGames"
        :key="game.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
        class="mb-4"
      >
        <b-card
          :title="game.title"
          class="h-100"
          :img-src="game.image_url"
          img-alt="Game image"
          img-top
        >
          <b-card-text class="mb-1">
            {{ game.description }}
          </b-card-text>
          <p class="mb-1"><strong>💵 Precio:</strong> ${{ game.price }}</p>
          <p class="mb-1"><strong>📂 Categoría:</strong> {{ game.category?.name }}</p>
          <p class="mb-2"><strong>📅 Lanzamiento:</strong> {{ formatDate(game.release_date) }}</p>

          <router-link :to="`/game/${game.id}`" class="btn btn-link p-0">Detalles</router-link>

          <div class="mt-3 d-grid gap-2">
            <b-button
              v-if="isAuthenticated && !isInCart(game.id) && !isPurchased(game.id)"
              variant="primary"
              @click="addToCart(game.id)"
            >
              Añadir al carrito
            </b-button>

            <b-alert
              v-else-if="isAuthenticated && isPurchased(game.id)"
              variant="success"
              show
              class="p-2 text-center"
            >
              ✅ Ya en tu biblioteca
            </b-alert>

            <b-alert
              v-else-if="isAuthenticated && isInCart(game.id)"
              variant="warning"
              show
              class="p-2 text-center"
            >
              🛒 Ya en tu carrito
            </b-alert>

            <b-button
              v-if="isAuthenticated"
              :variant="isFavorite(game.id) ? 'danger' : 'outline-danger'"
              @click="toggleFavorite(game)"
            >
              {{ isFavorite(game.id) ? 'Quitar de Favoritos' : 'Añadir a Favoritos' }}
            </b-button>
          </div>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
import { useGamesLogic } from '@/composables/useGamesLogic'
import { useAuthStore } from '@/store/auth'
import { computed } from 'vue'

</script>
