<template>
  <div id="app">
    <div class="logo">
      <h1>Vue.js Custom Form</h1>
    </div>
    <form-config-provider />
  </div>
</template>

<script>
import FormConfigProvider from "./components/FormConfigProvider.vue"
// import vm from "./backend/index.js" // temp
import { mapActions } from "vuex"
import axios from "axios"

export default {
  name: "app",
  components: {
    FormConfigProvider
  },
  created() {
    this.getQuestions()
  },
  data() {
    return {
      formData: {}
    }
  },
  beforeMount() {
    this.getData()
  },
  methods: {
    ...mapActions({ getQuestions: "lead/getQuestions" }),
    async getData() {
      await axios
        .get("https://wagtail-form-generator.herokuapp.com/api/v2/pages/4/") // heroku build
        // .get("http://localhost:8000/api/v2/pages/20/")    ||||| LOCAL
        .then(response => {
          this.formData = response.data.content
        })
        .catch(error => console.log(error)) //eslint-disable-line

      // console.log(this.$formData) //eslint-disable-line
    }
  }
}
</script>
<style>
@import "./assets/styles/main.css";
@import url("https://cdn.jsdelivr.net/npm/animate.css@3.5.1");
</style>
