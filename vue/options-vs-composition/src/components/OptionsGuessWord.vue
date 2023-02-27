<template>
  <div>
    <p class="text-lg my-4">Palavra digitada: {{ word }}</p>
  </div>
</template>

<script>
  export default {
    name: 'OptionsGuessWord',
    props: {
      word: {
        type: String,
        required: true,
        validator(value) {
          return (value === '' || /^[A-Z]+$/.test(value));
        }
      }
    }
  }
</script>
