import Vue from "vue"
import App from "./App.vue"

// 声明使用插件
import VueResource from "vue-resource"
Vue.use(VueResource)

new Vue({
    el: "#app",
    components:{
        App
    },
    template: "<App/>"
})