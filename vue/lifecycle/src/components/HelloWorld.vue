<template>
  <div class="hello">
    <h1>hello</h1>
    <input type="text" v-model=" aaa">
    {{ this.output }}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      aaa: ''
    }
  },
  computed: {
    output() {
      return this.aaa
    }
  },
  created() {
    console.log('created')
  },
  mounted() {
    console.log('mounted')
  },
  updated() {
    console.log('updated')
  },
}
</script>


<style scoped>

</style>
