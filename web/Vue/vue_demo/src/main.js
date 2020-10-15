import Vue from "vue"
import App from "./App.vue"

// 引入路由器
import router from "./routers"
new Vue({
    // 配置对象的属性名不能随意修改（其实是内置的key）
    el: "#app",
    components: {
        App
    },
    template: "<App/>",
    router: router
})