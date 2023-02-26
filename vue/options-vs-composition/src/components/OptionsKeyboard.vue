<template>
  <div>
    <div class="grid grid-cols-10 gap-3">
      <button
        v-for="letter in alphabet"
        :key="letter"
        class="border border-solid border-white rounded-md  text-xl text-center"
        @click="selectLetter(letter)"
      >
        {{ letter }}
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'OptionsKeyboard',
    data() {
      return {
        alphabet: ''
      };
    },
    mounted() {
      // create alphabet from A to Z
      for (let index = 65; index <= 90; index++) {
        this.alphabet += String.fromCharCode(index)
      }
    },
    methods: {
      // select clicked letter
      selectLetter(letter) {
        console.log(letter);
      }
    }
  }
</script>
