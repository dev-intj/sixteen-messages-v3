<template>
  <graphicalRepresentation/>
  <graphicalInterface/>
</template>

<script>
import graphicalRepresentation from './pages/graphicalRepresentation.vue'

import graphicalInterface from './components/graphicalComponents/graphicalInterface.vue'

// axios settings and import
import axiosApi from 'axios'

const axios = axiosApi.create({
    baseURL:`http://localhost:8000`,
    headers:{ 
      //responseType: "json",
      //xsrfCookieName: "csrftoken",
      //xsrfHeaderName: "X-CSRFToken", 
      }
});

window.axios = axios;

export default {
  name: 'app',
  components: {
    graphicalRepresentation,
    graphicalInterface
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
