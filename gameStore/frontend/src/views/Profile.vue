<template>
  <div>
    <h2>My Profile</h2>

    <div v-if="user && profile">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p v-if="profile.address"><strong>Address:</strong> {{ profile.address }}</p>
      <p v-if="profile.phone"><strong>Phone:</strong> {{ profile.phone }}</p>
      <p><strong>Balance:</strong> ${{ profile.balance }}</p>

      <div style="margin-top: 20px;">
        <h3>Recharge Balance</h3>
        <input
          type="number"
          v-model.number="rechargeAmount"
          placeholder="Amount to add"
          min="1"
        />
        <button @click="rechargeBalance" :disabled="!validAmount">Add</button>

        <p v-if="successMessage" style="color: green;">{{ successMessage }}</p>
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
      </div>

    </div>

  </div>
</template>

