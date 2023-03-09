<template>
  <div>
    <div class="grid grid-cols-10 gap-3 mb-4">
      <button
        v-for="letter in alphabet"
        :key="letter"
        :disabled="disable"
        class="border border-solid border-white rounded-md  text-xl text-center"
        :class="disable ? 'opacity-50' : ''"
        @click="$emit('updateGuessedWord', letter)"
      >
        {{ letter }}
      </button>
    </div>
    <div class="grid grid-cols-2 gap-3">
      <button
        :class="disable ? 'button_filled_disabled' : 'button_filled_default'"
        :disabled="disable"
        @click="$emit('deleteLastLetter')"
      >
        Apagar
      </button>
      <button
        :class="disable ? 'button_filled_disabled' : 'button_filled_inverted'"
        :disabled="disable"
        @click="$emit('checkGuessedWord')"
      >
       Enviar 
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'OptionsKeyboard',
    props: {
      disable: { type: Boolean, required: true }
    },
    data() {
      return {
        alphabet: ''
      };
    },
    emits: [
      'deleteLastLetter',
      'checkGuessedWord',
      'updateGuessedWord'
    ],
    mounted() {
      // create alphabet from A to Z
      for (let index = 65; index <= 90; index++) {
        this.alphabet += String.fromCharCode(index)
      }
    }
  }
</script>
