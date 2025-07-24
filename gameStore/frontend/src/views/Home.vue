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


  </b-container>
</template>

<script setup>

</script>
