<template>
  <div class="container">
    <Header title='Task Tracker'/>
  </div>
</template>


<script>
import Header from './components/Header.vue'


export default {
  name: 'App',
  components: {
    Header,
  },
  data() {
    return {
      tasks: []
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

.container {
  border: 1px solid black;
  border-radius: 5px;
  padding: 30px;
}

</style>
