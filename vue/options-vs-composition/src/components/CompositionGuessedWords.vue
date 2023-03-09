<script setup>
  import CompositionGuessWord from './CompositionGuessWord.vue'

  defineProps({
    guessedWords: {
      type: Array,
      required: true
    },

    chosenLetterIndex: {
      type: Number,
      required: true
    },

    userRound: {
      type: Number,
      required: true
    }
  });

  const emit = defineEmits([
    'updateChosenLetterIndex'
  ]);
</script>

<template>
  <div>
    <CompositionGuessWord
      v-for="word, index in guessedWords"
      :key="index"
      :word="word"
      :chosenLetterIndex="chosenLetterIndex"
      :active="index === userRound - 1"
      @updateChosenLetterIndex="emit('updateChosenLetterIndex', $event)"
    />
  </div>
</template>

