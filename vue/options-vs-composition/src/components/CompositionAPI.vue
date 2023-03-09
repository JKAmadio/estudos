<script setup>
  import { ref, reactive } from 'vue';
  import CompositionKeyboard from './CompositionKeyboard.vue';
  import CompositionGuessedWords from './CompositionGuessedWords.vue';

  //game setup variables
  let dailyWord = 'CASAL';
  let dailyWordLength = dailyWord.length;
  let totalRounds = 5;
  let userRound = ref(1);

  //user interactions variables
  let chosenLetterIndex = ref(0);
  let guessedWords = reactive([
    '     ',
    '     ',
    '     ',
    '     ',
    '     ',
  ])
  let isGuessRight = ref(null);

  /***********************************
   * INTERAÇOES COM O TECLADO
   **********************************/
  function updateGuessedWord(letter) {
    let currentWordActive = guessedWords[userRound.value - 1];
    let newWord = '';
    //se o index escolhido for igual ao index da letra na palavra substituimos pela letra escolhida
    for (let index in currentWordActive) {
      Number(index) === chosenLetterIndex.value ?
        newWord += letter :
        newWord += currentWordActive[index];
    }
    guessedWords[userRound.value - 1] = newWord;

    moveToNextGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
    isGuessRight.value = null;
  }

  function deleteLastLetter() {
    let currentWordActive = guessedWords[userRound.value - 1];
    let newWord = '';
    // se o index escolhido for igual ao index da letra na palavra substituímos por um vazio
    for (let index in currentWordActive) {
      Number(index) === chosenLetterIndex.value ?
        newWord += ' ' :
        newWord += currentWordActive[index];
    }
    guessedWords[userRound.value - 1] = newWord;
    
    moveToPrevGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
    isGuessRight.value = null;
  }

  /***********************************
   * INTERAÇOES PALAVRA ADIVINHADA
   **********************************/
  function checkGuessedWord() {
    if (guessedWords.includes(dailyWord))
      isGuessRight.value = true;
    else if (userRound.value === totalRounds)
      isGuessRight.value = false;
    else {
      userRound.value += 1;
      chosenLetterIndex.value = 0;
    }
  }

  function moveToNextGuessedLetter() {
    // selecionamos o próximo espaço de letra
    // não tem próximo se está no último espaço disponível
    if (chosenLetterIndex.value < dailyWordLength - 1)
      chosenLetterIndex.value += 1;
  }

  function moveToPrevGuessedLetter() {
    // selecionamos o espaço de letra anterior
    // não tem anterior se é o primeiro espaço disponível
    if (chosenLetterIndex.value > 0)
      chosenLetterIndex.value -= 1;
  }
</script>

<template>
  <div>
    <CompositionGuessedWords
      :guessedWords="guessedWords"
      :chosenLetterIndex="chosenLetterIndex"
      :userRound="userRound"
      @updateChosenLetterIndex="chosenLetterIndex = $event"
    />
    <CompositionKeyboard
      :disable="isGuessRight === true || isGuessRight === false"
      @updateGuessedWord="updateGuessedWord($event)"
      @checkGuessedWord="checkGuessedWord"
      @deleteLastLetter="deleteLastLetter"
    />
    <p v-if="isGuessRight === true">PARABÉNS VOCÊ ACERTOU!</p>
    <p v-else-if="isGuessRight === false">SUAS CHANCES ACABARAM!</p>
  </div>
</template>

