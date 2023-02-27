<script setup>
  defineProps({
    word: {
      type: String,
      required: true,
      validator(value) {
        return (value === '' || /^[A-Z]+$/.test(value));
      }
    }
  });
</script>

<template>
  <div>
    <p class="my-4 text-lg">Palavra digitada: {{ word }}</p>
  </div>
</template>

