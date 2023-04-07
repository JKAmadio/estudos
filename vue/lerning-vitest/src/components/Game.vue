<template>
  <div>
    <Navbar
      :userEmail="user.email"
      :showLogin="showLogin"
      @updateShowLogin="showLogin = !showLogin"
    />
    <Login
      v-if="showLogin"    
      :user="user"
    />
  </div>
</template>

<script>
import Navbar from './Navbar.vue'
import Login from './Login.vue'
export default {
  components: {
    Login,
    Navbar
  },
  data() {
    return {
      showLogin: false,
      user: {
        email: '',
        password: ''
      }
    }
  },
}
</script>
