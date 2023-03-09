<template>
  <div>
    <OptionsGuessWord
      v-for="word, index in guessedWords"
      :key="index"
      :word="word"
      :chosenLetterIndex="chosenLetterIndex"
      :active="index === userRound - 1"
      @updateChosenLetterIndex="$emit('updateChosenLetterIndex', $event)"
    />
  </div>
</template>

<script>
  import OptionsGuessWord from './OptionsGuessWord.vue'

  export default {
    name: 'OptionsGuessedWords',
    components: {
      OptionsGuessWord
    },
    props: {
      guessedWords: {
        type: Array,
        required: true
      },

      chosenLetterIndex: {
        type: Number,
        required: true,
        validator(value) {
          return (value >= 0 || value < 5);
        }
      },

      userRound: {
        type: Number,
        required: true
      }
    },
    emits: [
      'updateChosenLetterIndex'
    ]
  }
</script>
