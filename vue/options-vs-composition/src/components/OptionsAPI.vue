<template>
  <div>
    <OptionsGuessWord
      :word="word"
    />
    <OptionsKeyboard
      :disable="disableKeyboard"
      @updateGuessedWord="updateGuessedWord($event)"
      @checkGuessedWord="checkGuessedWord"
      @deleteLastLetter="deleteLastLetter"
    />
    <p v-if="isGuessRight === true">PARABÉNS VOCÊ ACERTOU!</p>
    <p v-else-if="isGuessRight === false">ESSA NÃO É A PALAVRA CERTA</p>
  </div>
</template>

<script>
import OptionsKeyboard from './OptionsKeyboard.vue'
import OptionsGuessWord from './OptionsGuessWord.vue'

export default {
  name: 'OptionsAPI',
  components: {
    OptionsKeyboard,
    OptionsGuessWord
  },
  data() {
    return {
      dailyWord: 'CASAL',
      dailyWordLength: 0,
      word: '',
      isGuessRight: null
    };
  },
  computed: {
    disableKeyboard() {
      return this.word.length >= this.dailyWordLength ? true : false
    }
  },
  mounted() {
    this.dailyWordLength = this.dailyWord.length
  },
  methods: {
    updateGuessedWord(letter) {
      this.word += letter;
      this.isGuessRight = null;
    },

    deleteLastLetter() {
      this.word = this.word.slice(0, -1);
      this.isGuessRight = null;
    },

    checkGuessedWord() {
      this.isGuessRight = this.word === this.dailyWord;
    }
  }
}
</script>
