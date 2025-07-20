<template>
  <div class="register-container">
    <h2>Registro de Usuario</h2>

    <form @submit.prevent="register" class="register-form">
      <input v-model="username" placeholder="Nombre de usuario" required />
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

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const address = ref('')
const phone = ref('')
const error = ref('')
const success = ref(false)

const register = async () => {
  error.value = ''
  success.value = false
  try {
    await api.post('/api/register/', {
      username: username.value,
      email: email.value,
      password: password.value,
      address: address.value,
      phone: phone.value
    })

    const response = await api.post('/api/token/', {
      username: username.value,
      password: password.value
    })

    const { access, refresh } = response.data
    localStorage.setItem('access', access)
    localStorage.setItem('refresh', refresh)

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
.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
}

.register-form input {
  display: block;
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
}

button {
  padding: 0.6rem 1.2rem;
  background-color: #2e7d32;
  color: white;
  border: none;
  cursor: pointer;
}

.error-message {
  color: red;
  margin-top: 1rem;
}

.success-message {
  color: green;
  margin-top: 1rem;
}
</style>
