<template>
  <div>
    <h2>
      Options API
    </h2>
    <p>{{ counter }}</p>
    <button @click="handleClick">botão</button>
  </div>
</template>

<script>
export default {
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
