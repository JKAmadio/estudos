<script setup>
  import { ref } from 'vue';
  import OptionsAPI from './components/OptionsAPI.vue'
  import CompositionAPI from './components/CompositionAPI.vue'

  let visibleAPI = ref('options');

  const changeVisibleAPI = (newAPI) => {
    visibleAPI.value = newAPI;
  }

</script>

<template>
  <main>
    <header>
      <button @click="changeVisibleAPI('options')">
        Options
      </button>
      <button @click="changeVisibleAPI('composition')">
        Composition
      </button>
    </header>
    <div>
      <OptionsAPI v-if="visibleAPI === 'options'"/>
      <CompositionAPI  v-if="visibleAPI === 'composition'"/>
    </div>
  </main>
</template>

