<script setup>
  defineProps({
    word: {
      type: String,
      required: true,
      validator(value) {
        return (/^[A-Z\s]+$/.test(value));
      }
    },

    chosenLetterIndex: {
      type: Number,
      required: true,
      validator(value) {
        return (value >= 0 || value < 5);
      }
    },

    active: {
      type: Boolean,
      required: true
    }
  });

  const emit = defineEmits([
    'updateChosenLetterIndex'
  ]);
</script>

<template>
  <div class="grid grid-cols-5 gap-3 my-4">
    <button
      v-for="letter, index in word"
      :key="index"
      class="rounded-md bg-white"
      :class="{
        'opacity-10 text-gray-900' : !active,
        'bg-opacity-70 text-black' : active && chosenLetterIndex === index,
        'bg-opacity-30 text-white' : active && chosenLetterIndex !== index,
      }"
      @click="emit('updateChosenLetterIndex', index)"
    >
      {{ letter }}.
    </button>
  </div>
</template>

