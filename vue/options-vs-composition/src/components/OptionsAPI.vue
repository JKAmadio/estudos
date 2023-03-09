<template>
  <div>
    <OptionsGuessedWords
      :guessedWords="guessedWords"
      :chosenLetterIndex="chosenLetterIndex"
      :userRound="userRound"
      @updateChosenLetterIndex="chosenLetterIndex = $event"
    />
    <OptionsKeyboard
      :disable="isGuessRight === true"
      @updateGuessedWord="updateGuessedWord($event)"
      @checkGuessedWord="checkGuessedWord"
      @deleteLastLetter="deleteLastLetter"
    />
    <p v-if="isGuessRight === true">PARABÉNS VOCÊ ACERTOU!</p>
    <p v-else-if="isGuessRight === false">SUAS CHANCES ACABARAM!</p>
  </div>
</template>

<script>
import OptionsKeyboard from './OptionsKeyboard.vue'
import OptionsGuessedWords from './OptionsGuessedWords.vue'

export default {
  name: 'OptionsAPI',
  components: {
    OptionsKeyboard,
    OptionsGuessedWords
  },
  data() {
    return {
      dailyWord: 'CASAL',
      dailyWordLength: 0,
      totalRounds: 5,
      userRound: 1,

      chosenLetterIndex: 0,
      guessedWords: [
        '     ',
        '     ',
        '     ',
        '     ',
        '     '
      ],
      isGuessRight: null
    };
  },
  mounted() {
    this.dailyWordLength = this.dailyWord.length;
  },
  methods: {
    updateGuessedWord(letter) {
      let currentWordActive = this.guessedWords[this.userRound - 1];
      let newWord = '';
      for (let index in currentWordActive) {
        Number(index) === this.chosenLetterIndex ?
          newWord += letter :
          newWord += currentWordActive[index];
      }
      this.guessedWords[this.userRound - 1]= newWord;

      this.moveToNextGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
      this.isGuessRight = null;
    },

    deleteLastLetter() {
      let currentWordActive = this.guessedWords[this.userRound - 1];
      let newWord = '';
      for (let index in currentWordActive) {
        Number(index) === this.chosenLetterIndex ?
          newWord += ' ' :
          newWord += currentWordActive[index];
      }
      this.guessedWords[this.userRound - 1] = newWord;
      
      this.moveToPrevGuessedLetter();
      
      // zeramos a variável para remover qualquer uma das respostas
      this.isGuessRight = null;
    },

    checkGuessedWord() {
      if (this.guessedWords.includes(this.dailyWord))
        this.isGuessRight = true;
      else if (this.userRound === this.totalRounds)
        this.isGuessRight = false;
      else {
        this.userRound += 1;
        this.chosenLetterIndex = 0;
      }
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
