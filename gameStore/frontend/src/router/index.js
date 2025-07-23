import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Profile from '@/views/Profile.vue'
import CartView from '@/views/CartView.vue'
import GameDetail from '@/views/GameDetail.vue'
import LibraryView from '@/views/LibraryView.vue'
import Categories from '@/views/Categories.vue'
import CategoryGames from '@/views/CategoryGames.vue'

const requireAuth = (to, from, next) => {
  const auth = useAuthStore()
  if (auth.isAuthenticated) {
    next()
  } else {
    next('/login')
  }
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/profile',            
    name: 'Profile',
    component: Profile,
    beforeEnter: requireAuth
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartView,
    beforeEnter: requireAuth
  },
  {
    path: '/game/:id',
    name: 'GameDetail',
    component: GameDetail
  },
  {
    path: '/library',            
    name: 'Library',
    component: LibraryView,
    beforeEnter: requireAuth
  },
  { 
    path: '/categories', 
    name: 'Categories', 
    component: Categories 
  },
  { 
    path: '/category/:id', 
    name: 'CategoryGames', 
    component: CategoryGames 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
