<template>
  <div>
    <div class="w-fit mx-auto mt-12 flex items-center space-x-4">
      <button
        v-for="letter, index in guessedWord"
        :key="index"
        :id="`tile-button-${index}`"
        class="p-10 border-2 rounded-md text-2xl font-bold leading-none font-mono"
        :class="{
          'border-white text-white' : tileSelectedIndex === index,
          'border-gray-600 text-gray-600' : tileSelectedIndex !== index
        }"
        @keydown="updateTile"
        @click="tileSelectedIndex = index"
      >
        {{ letter.toUpperCase() }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tiles',
  data() {
    return {
      guessedWord: '#####',
      tileSelectedIndex: 0
    } 
  },
  methods: {
    updateTile(e) {
      const keyValue= e.key;

      if (this.tileSelectedIndex === null)
        return;

      // se usuário clicou em alguma letra
      if (keyValue.length === 1 && keyValue.match(/[a-z]/i)) {
        //todo: check test file and make commented test pass

        this.guessedWord = this.guessedWord.substring(0, this.tileSelectedIndex) + keyValue + this.guessedWord.substring(this.tileSelectedIndex + 1);
      
        for (let letter in this.guessedWord) {
          letter = Number(letter);
          // remove tile selections when all tiles are filled
          if (!this.guessedWord.includes('#')) {
            this.tileSelectedIndex = null;
            break;
          }
          // reset tile index to 0 when analysing last letter
          if (letter === this.guessedWord.length - 1)
            this.tileSelectedIndex = 0;
          // set tileSelectedIndex to next empty tile
          if (this.guessedWord[this.tileSelectedIndex + letter + 1] === '#') {
            this.tileSelectedIndex = this.tileSelectedIndex + letter + 1;
            break;
          }
        }
      }
      else if (keyValue === 'Backspace') {
        for (let letter in this.guessedWord) {
          letter = Number(letter)
          // if tile is not empty dont change selected tile
          if (this.guessedWord[this.tileSelectedIndex] !== '#')
            break;
          // reset tile index to last tile when analysing first letter
          if (this.tileSelectedIndex - letter - 1 < 0)
            this.tileSelectedIndex = this.guessedWord.length;
          // set tileSelectedIndex to previous empty tile
          if (this.guessedWord[this.tileSelectedIndex - letter - 1] !== '#' ||
              this.guessedWord === '#####'
          ) {
            this.tileSelectedIndex = this.tileSelectedIndex - letter - 1;
            break;
          }
        }
        
        // reset tile only if needed
        if (this.guessedWord !== '#####')
          this.guessedWord = this.guessedWord.substring(0, this.tileSelectedIndex) + '#' + this.guessedWord.substring(this.tileSelectedIndex + 1);
      }
    }
  },
}
</script> 

