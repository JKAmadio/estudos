<template>
  <div>
    <Navbar
      :userEmail="user.email"
      :showLogin="showLogin"
      @updateShowLogin="methodUpdateShowLogin"
    />
    <Login
      v-if="!isLogged && showLogin"    
      :user="user"
      @updateIsLogged="isLogged = true"
    />
    <div v-if="isLogged">
      you are logged
    </div>
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
      isLogged: false,
      user: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    methodUpdateShowLogin() {
      this.showLogin = !this.showLogin;
    }
  }
}
</script>
