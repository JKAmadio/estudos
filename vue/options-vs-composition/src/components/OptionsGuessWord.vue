<template>
  <div>
    <p class="my-4 text-lg">Palavra digitada: {{ word }}</p>
    <div class="grid grid-cols-5 gap-3 my-4">
      <button
        v-for="letter, index in word"
        :key="index"
        class="rounded-md bg-white"
        :class="chosenLetterIndex === index ? 'bg-opacity-70 text-black' : 'bg-opacity-30 text-white'"
        @click="$emit('updateChosenLetterIndex', index)"
      >
        {{ letter }}.
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'OptionsGuessWord',
    props: {
      word: {
        type: String,
        required: true,
        validator(value) {
          return (/^[A-Z\s]+$/.test(value));
        }
      },

      chosenLetterIndex: {
        type: Number,
        required: true,
        validator(value) {
          return (value >= 0 || value < 5);
        }
      }
    },
    emits: [
      'updateChosenLetterIndex'
    ]
  }
</script>
