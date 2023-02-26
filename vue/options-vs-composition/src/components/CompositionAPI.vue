<script setup>
  import { ref } from 'vue';
  import CompositionKeyboard from './CompositionKeyboard.vue';

  let counter = ref(0);

  const handleClick = () => {
    counter.value += 1;
  }
</script>

<template>
  <div>
    <h2>
      Composition component
    </h2>
    <p>{{ counter }}</p>
    <button @click="handleClick">botão</button>
    <CompositionKeyboard/>
  </div>
</template>

