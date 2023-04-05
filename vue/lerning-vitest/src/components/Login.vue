<template>
  <div class="p-16 flex flex-col items-center">
    <form @submit="sendLoginRequest">
      <div class="flex flex-col">
        <p>Email</p>
        <input
          v-model.lazy="user.email"
          class="w-60 px-2 py-1 rounded-sm text-black"
          :class="errors.email ? 'bg-red-200' : ''"
          type="email"
        />
      </div>
      <div class="flex flex-col">
        <p>Senha</p>
        <input
          v-model.lazy="user.password"
          class="w-60 px-2 py-1 rounded-sm text-black"
          :class="errors.password ? 'bg-red-200' : ''"
          type="password"
        />
      </div>
      <button
        type="submit"
        class="test_button mt-3 px-6 py-2 border-2 border-solid border-green-700 rounded-md bg-green-700 hover:bg-transparent"
        @click="sendLoginRequest"
      >
        Entrar
      </button>
    </form>
    <p>Email: {{ user.email }} erro: {{ errors.email }}</p>
    <p>Senha: {{ user.password }} erro: {{ errors.password }}</p>
  </div>
</template>

<script>
export default {
  props: {
    user: { type: Object, required: true }
  },
  data() {
    return {
      'errors': {
        'email': false,
        'password': false
      }
    }
  },
  methods: {
    sendLoginRequest() {
      this.checkEmailFormat();
      this.checkPasswordFormat();
    },

    checkEmailFormat() {
      if (!this.user.email.includes('@'))
        this.errors.email = true;
      else
        this.errors.email = false;
    },

    checkPasswordFormat() {
      if (this.user.password.length < 8)
        this.errors.password = true;
      else
        this.errors.password = false;
    }
  }
}
</script>
