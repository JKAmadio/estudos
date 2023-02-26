<script setup>
  import { ref, onMounted } from 'vue';
  
  // create alphabet from A to Z
  let alphabet = ref('');

  onMounted(() => {
    for (let index = 65; index <= 90; index++) {
      alphabet.value += String.fromCharCode(index)
    }
  })

  // select clicked letter
  function selectLetter(letter) {
    console.log(letter);
  }
</script>

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

