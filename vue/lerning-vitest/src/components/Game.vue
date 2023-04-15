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
    <Tiles
    />
  </div>
</template>

<script>
import Navbar from './Navbar.vue'
import Login from './Login.vue'
import Tiles from './Tiles.vue'
export default {
  components: {
    Login,
    Navbar,
    Tiles
  },
  data() {
    return {
      // user
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
