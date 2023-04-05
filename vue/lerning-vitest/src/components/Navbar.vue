<template>
  <div class="px-48 py-4 flex items-center justify-between bg-opacity-10 bg-white">
    <p>{{ userEmail }}</p>
    <button
      class="px-3 py-1 border-2 border-solid border-green-700 rounded-md bg-green-700 hover:bg-transparent"
      @click="$emit('showLogin')"
    >
      Login
    </button>
  </div>
</template>

<script>
export default {
  props: {
    userEmail: { type: String, required: false, default: 'fulano@email.com' }
  },
  emits: [
    'showLogin'
  ]
}
</script>

