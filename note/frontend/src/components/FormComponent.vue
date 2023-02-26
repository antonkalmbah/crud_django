<template>
  <div>
    <thead>
        <a href="http://127.0.0.1:8000/admin/">Ссылка в админ-панель</a><hr>
    </thead>
    <tbody>
      <h1>Заголовок в FormComponent.vue</h1>
    </tbody>
    <div>
      <ul v-for="i in info">
        <li>{{ i.name }}</li>
        <li>{{ i.second_name }}</li>
        <li>{{ i.age }}</li>
      </ul>
    </div>
    <div>
      {{ getInfo }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FormComponent',
  data() {
    return {
      info: [
        {
          name: 'Anton',
          second_name: 'Kalmbakh',
          age: 27
        } 
      ]
    }
  },
  mounted() {
    
  },
  methods: {
    getInfo() {
      axios.get('http://127.0.0.1:8000/api/')
    }
  }
}

</script>

<style>

</style>