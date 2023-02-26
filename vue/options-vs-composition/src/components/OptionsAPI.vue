<template>
  <div>
    <h2>
      Options API
    </h2>
    <p>{{ counter }}</p>
    <button @click="handleClick">botão</button>
    <OptionsKeyboard/>
  </div>
</template>

<script>
import OptionsKeyboard from './OptionsKeyboard.vue'
export default {
  name: 'OptionsAPI',
  components: {
    OptionsKeyboard
  },
  data() {
    return{
      counter: 0
    };
  },
  methods: {
    handleClick() {
      this.counter = this.counter + 1;
    }
  }
}
</script>
