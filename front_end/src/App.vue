<template>
  <graphicalRepresentation/>
</template>

<script>
import graphicalRepresentation from './pages/graphicalRepresentation.vue'
export default {
  name: 'app',
  components: {
    graphicalRepresentation
  }
}
</script>

<style>
body {
  margin: 0;
}
canvas {
  display: block;
}
</style>
