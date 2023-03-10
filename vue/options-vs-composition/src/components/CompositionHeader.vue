<script setup>
  defineProps({
    levels: {
      type: Array,
      required: true
    },
    currentLevel: {
      type: Number,
      required: true
    }
  })

  const emit = defineEmits([
    'updateCurrentLevel'
  ])
</script>

<template>
  <div class="py-6 px-4 rounded-md bg-white bg-opacity-10">
    <div class="flex items-center space-x-4">
      <button
        v-for="level, index in levels"
        :key="index"
        :class="{
          'underline underline-offset-4 font-bold' : currentLevel === index
        }"
        @click="emit('updateCurrentLevel', index)"
      >
        {{ level['name'] }}
      </button>
    </div>
  </div>
</template>

