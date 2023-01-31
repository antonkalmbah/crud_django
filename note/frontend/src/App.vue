<template>
  <div>
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios'
export default {
  name: 'App',
  components: [
    HelloWorld
  ],
  data: {
    getIndex() {
      const url = `http://localhost:8000/api/index/`;
      return axios.get(url).then(response => response.data);
    }
  }

}
</script>

<style>
</style>
