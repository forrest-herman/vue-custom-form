import Vue from "vue"
import App from "./App.vue"

import store from "./store"
import VeeValidate from "vee-validate"
import { BootstrapVue, IconsPlugin } from "bootstrap-vue"
// import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

import "./directives"
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VeeValidate)

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App)
}).$mount("#app")
