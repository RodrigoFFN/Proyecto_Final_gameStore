<template>
  <div class="login-container">
    <h2>Inicio de Sesión</h2>

    <form @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Usuario" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button type="submit">Iniciar Sesión</button>
    </form>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')

const handleLogin = async () => {
  const success = await auth.login(username.value, password.value)
  if (success) {
    router.push('/')
  } else {
    alert('Credenciales incorrectas')
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.login-container {
  max-width: 400px;
  margin: 5rem auto;
  padding: 2rem;
  background-color: #2b2b2b;
  border: 1px solid #44f2ff;
  border-radius: 12px;
  box-shadow: 0 0 12px #44f2ff33;
  font-family: 'Press Start 2P', monospace;
  color: #f0f0f0;
  text-align: center;
}

h2 {
  color: #44f2ff;
  margin-bottom: 2rem;
  font-size: 1rem;
  text-shadow: 1px 1px #000;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

input {
  padding: 0.75rem;
  font-size: 0.7rem;
  border-radius: 8px;
  border: 1px solid #44f2ff;
  background-color: #1f1f1f;
  color: #cfffff;
  font-family: 'Press Start 2P', monospace;
  outline: none;
}

input::placeholder {
  color: #a0ffff;
  opacity: 0.6;
}

button {
  padding: 0.75rem;
  font-size: 0.8rem;
  border: none;
  border-radius: 8px;
  background-color: #ff3366;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-family: 'Press Start 2P', monospace;
}

button:hover {
  background-color: #ff5a7d;
  box-shadow: 0 0 8px #ff3366aa;
}
</style>
