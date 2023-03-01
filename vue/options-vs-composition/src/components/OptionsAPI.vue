<template>
  <div>
    <OptionsGuessWord
      :word="word"
      :chosenLetterIndex="chosenLetterIndex"
      @updateChosenLetterIndex="chosenLetterIndex = $event"
    />
    <OptionsKeyboard
      :disable="isGuessRight === true"
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
      word: '     ',
      chosenLetterIndex: 0,
      isGuessRight: null
    };
  },
  mounted() {
    this.dailyWordLength = this.dailyWord.length
  },
  methods: {
    updateGuessedWord(letter) {
      let newWord = '';
      for (let index in this.word) {
        Number(index) === this.chosenLetterIndex ?
          newWord += letter :
          newWord += this.word[index];
      }
      this.word = newWord;

      this.moveToNextGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
      this.isGuessRight = null;
    },

    deleteLastLetter() {
      let newWord = '';
      for (let index in this.word) {
        Number(index) === this.chosenLetterIndex ?
          newWord += ' ' :
          newWord += this.word[index];
      }
      this.word = newWord;
      
      this.moveToPrevGuessedLetter();
      
      // zeramos a variável para remover qualquer uma das respostas
      this.isGuessRight = null;
    },

    checkGuessedWord() {
      this.isGuessRight = this.word === this.dailyWord;
    },

    moveToNextGuessedLetter() {
      if (this.chosenLetterIndex < this.dailyWordLength -1)
      this.chosenLetterIndex += 1;
    },

    moveToPrevGuessedLetter() {
      if (this.chosenLetterIndex > 0)
        this.chosenLetterIndex -= 1;
    }
  }
}
</script>
