<template>
  <div>
    <h2>Your Cart</h2>

    <div v-if="items.length === 0">
      Your cart is empty.
    </div>
    <div v-else>
      <div v-for="item in items" :key="item.id">
        <p>
          {{ item.videogame.title }} - ${{ item.videogame.price }} x {{ item.quantity }}
        </p>
        <button @click="removeItem(item.id)">Remove</button>
      </div>

      <p><strong>Total:</strong> ${{ total }}</p>

      <button @click="checkout" :disabled="items.length === 0">Buy</button>

      <p v-if="successMessage" style="color: green;">{{ successMessage }}</p>
      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    </div>
  </div>
</template>