import Vue from "vue"
import App from "./App.vue"

// 引入组件库
import {Button} from "mint-ui"
// 注册为全局标签
// 其实每一个组件都由一个默认的标签, 通过Button.name来回去对应的属性, 具体可以见官网文档
Vue.component(Button.name, Button)

new Vue({
    el: "#app",
    components: {
        App
    },
    template: "<App/>"
})