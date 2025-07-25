<template>
  <div class="register-container">
    <h2>Registro de Usuario</h2>

    <form @submit.prevent="register" class="register-form">
      <input v-model="username" placeholder="Nombre" required />
      <input v-model="last_name" placeholder="Apellido" required />
      <input v-model="email" type="email" placeholder="Correo electrónico" required />
      <input v-model="password" type="password" placeholder="Contraseña" required />
      <input v-model="address" placeholder="Dirección" />
      <input v-model="phone" placeholder="Teléfono" />

      <button type="submit">Registrarse</button>
    </form>

    <p v-if="error" class="error-message">{{ error }}</p>
    <p v-if="success" class="success-message">Registro exitoso. Redirigiendo...</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api/api.js'
import { useAuthStore } from '@/store/auth.js'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const email = ref('')
const password = ref('')
const address = ref('')
const phone = ref('')
const last_name = ref('')
const error = ref('')
const success = ref(false)

const register = async () => {
  error.value = ''
  success.value = false

  try {
    const response = await api.post('/api/register/', {
      username: username.value,
      email: email.value,
      password: password.value,
      address: address.value,
      phone: phone.value,
      last_name: last_name.value
    })


    const { access, refresh } = response.data
    authStore.handleLoginTokens({
      access,
      refresh,
      username: username.value
    })

    success.value = true
    router.push('/')
  } catch (err) {
    if (err.response?.data) {
      error.value = JSON.stringify(err.response.data)
    } else {
      error.value = 'Error al registrar o autenticar usuario.'
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.register-container {
  max-width: 500px;
  margin: 4rem auto;
  padding: 2rem;
  background-color: #1c1c1c;
  border: 2px solid #00ffee;
  border-radius: 12px;
  box-shadow: 0 0 20px #00ffee66;
  font-family: 'Press Start 2P', monospace;
  color: #f0f0f0;
  text-align: center;
}

h2 {
  color: #00ffee;
  margin-bottom: 2rem;
  font-size: 1rem;
  text-shadow: 2px 2px #000;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.75rem;
  font-size: 0.7rem;
  border-radius: 8px;
  border: 1px solid #00ffee;
  background-color: #121212;
  color: #00ffee;
  outline: none;
  font-family: 'Press Start 2P', monospace;
}

input::placeholder {
  color: #66ffff;
  opacity: 0.6;
}

button {
  padding: 0.75rem;
  font-size: 0.8rem;
  border: none;
  border-radius: 8px;
  background-color: #ff0055;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-family: 'Press Start 2P', monospace;
}
</style>
