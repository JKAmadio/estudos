<script setup>
  import { ref, computed } from 'vue';
  import CompositionKeyboard from './CompositionKeyboard.vue';
  import CompositionGuessWord from './CompositionGuessWord.vue';

  //game setup variables
  let dailyWord = 'CASAL';
  let dailyWordLength = dailyWord.length;

  //user interactions variables
  let word = ref('     ');
  let chosenLetterIndex = ref(0);
  let isGuessRight = ref(null);

  /***********************************
   * INTERAÇOES COM O TECLADO
   **********************************/
  function updateGuessedWord(letter) {
    let newWord = '';
    //se o index escolhido for igual ao index da letra na palavra substituimos a letra
    for (let index in word.value) {
      Number(index) === chosenLetterIndex.value ?
        newWord += letter :
        newWord += word.value[index];
    }
    word.value = newWord;

    moveToNextGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
    isGuessRight.value = null;
  }

  function deleteLastLetter() {
    let newWord = '';
    // se o index escolhido for igual ao index da letra na palavra substituímos por um vazio
    for (let index in word.value) {
      Number(index) === chosenLetterIndex.value ?
        newWord += ' ' :
        newWord += word.value[index];
    }
    word.value = newWord;
    
    moveToPrevGuessedLetter();

    // zeramos a variável para remover qualquer uma das respostas
    isGuessRight.value = null;
  }

  /***********************************
   * INTERAÇOES PALAVRA ADIVINHADA
   **********************************/
  function checkGuessedWord() {
    isGuessRight.value = word.value === dailyWord;
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
    <CompositionGuessWord
      :word="word"
      :chosenLetterIndex="chosenLetterIndex"
      @updateChosenLetterIndex="chosenLetterIndex = $event"
    />
    <CompositionKeyboard
      :disable="isGuessRight === true"
      @updateGuessedWord="updateGuessedWord($event)"
      @checkGuessedWord="checkGuessedWord"
      @deleteLastLetter="deleteLastLetter"
    />
    <p v-if="isGuessRight === true">PARABÉNS VOCÊ ACERTOU!</p>
    <p v-else-if="isGuessRight === false">ESSA NÃO É A PALAVRA CERTA</p>
  </div>
</template>

