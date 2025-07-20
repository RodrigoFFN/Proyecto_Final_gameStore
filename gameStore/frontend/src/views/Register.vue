<script setup>
import { ref } from 'vue'
import axios from '@/api'
import { useRouter } from 'vue-router'
import api from '@/api'

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
    // Paso 1: Registrar
    await axios.post('/api/register/', {
      username: username.value,
      email: email.value,
      password: password.value,
      address: address.value,
      phone: phone.value
    })

    // Paso 2: Autenticar
    const response = await axios.post('/api/token/', {
      username: username.value,
      password: password.value
    })

    // Paso 3: Guardar token
    const { access, refresh } = response.data
    localStorage.setItem('access', access)
    localStorage.setItem('refresh', refresh)

    // Paso 4: Redirigir a inicio
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
