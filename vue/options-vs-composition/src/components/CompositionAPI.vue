<script setup>
  import { ref, computed } from 'vue';
  import CompositionKeyboard from './CompositionKeyboard.vue';
  import CompositionGuessWord from './CompositionGuessWord.vue';

  //game setup variables
  let dailyWord = 'CASAL';
  let dailyWordLength = dailyWord.length;

  //user interactions variables
  let word = ref('');
  let isGuessRight = ref(null);

  /***********************************
   * INTERAÇOES COM O TECLADO
   **********************************/
  function updateGuessedWord(letter) {
    word.value += letter;
    isGuessRight.value = null;
  }

  const disableKeyboard = computed(() => {
    return word.value.length >= dailyWordLength ? true : false
  })

  function deleteLastLetter() {
    word.value = word.value.slice(0, -1);
    isGuessRight.value = null;
  }

  function checkGuessedWord() {
    isGuessRight.value = word.value === dailyWord;
  }
</script>

<template>
  <div>
    <CompositionGuessWord
      :word="word"
    />
    <CompositionKeyboard
      :disable="disableKeyboard"
      @updateGuessedWord="updateGuessedWord($event)"
      @checkGuessedWord="checkGuessedWord"
      @deleteLastLetter="deleteLastLetter"
    />
    <p v-if="isGuessRight === true">PARABÉNS VOCÊ ACERTOU!</p>
    <p v-else-if="isGuessRight === false">ESSA NÃO É A PALAVRA CERTA</p>
  </div>
</template>

