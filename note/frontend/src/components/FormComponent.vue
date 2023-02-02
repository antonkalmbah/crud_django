<template>
  <div>
    <thead>
        <a href="/admin">Ссылка в админ-панель</a><hr>
    </thead>
    <tbody>
      <h1>Заголовок в FormComponent.vue</h1>
    </tbody>
    <div v-for="note in info.data">
      {{ note.id }}. {{ note.heading }} <br />
      {{ note.text }} 
      <button>delete</button>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FormComponent',
  data () {
    return {
      info: '',
      delete: null
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/')
      .then(response => (this.info = response.data)),

    axios
      .get('')
  }
}

</script>

</style>
