<script setup>
  import { ref, onMounted } from 'vue';

  defineProps({
    disable: { type: Boolean, required: true }
  });

  const emit = defineEmits([
    'updateGuessedWord',
    'checkGuessedWord',
    'deleteLastLetter'
  ]);

  // create alphabet from A to Z
  let alphabet = ref('');

  onMounted(() => {
    for (let index = 65; index <= 90; index++) {
      alphabet.value += String.fromCharCode(index);
    }
  });
</script>

<template>
  <div>
    <div class="grid grid-cols-10 gap-3 mb-4">
      <button
        v-for="letter in alphabet"
        :key="letter"
        :disabled="disable"
        class="border border-solid border-white rounded-md  text-xl text-center"
        :class="disable ? 'opacity-50' : ''"
        @click="emit('updateGuessedWord', letter)"
      >
        {{ letter }}
      </button>
    </div>
    <div class="grid grid-cols-2 gap-3">
      <button
        :class="disable ? 'button_filled_disabled' : 'button_filled_default'"
        :disabled="disable"
        @click="emit('deleteLastLetter')"
      >
        Apagar
      </button>
      <button
        :class="disable ? 'button_filled_disabled' : 'button_filled_inverted'"
        :disabled="disable"
        @click="emit('checkGuessedWord')"
      >
        Enviar
      </button>
    </div>
  </div>
</template>

