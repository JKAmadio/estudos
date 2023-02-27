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
    <header class="space-x-4">
      <button
        :class="visibleAPI === 'options' ? 'font-bold underline underline-offset-4' : ''"
        @click="changeVisibleAPI('options')"
      >
        Options
      </button>
      <button
        :class="visibleAPI === 'composition' ? 'font-bold underline underline-offset-4' : ''"
        @click="changeVisibleAPI('composition')"
      >
        Composition
      </button>
    </header>
    <div>
      <OptionsAPI v-if="visibleAPI === 'options'"/>
      <CompositionAPI  v-else-if="visibleAPI === 'composition'"/>
    </div>
  </main>
</template>

