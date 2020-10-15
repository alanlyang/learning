/**
 * 路由器模块
 */
import Vue from "vue"
import VueRouter from 'vue-router'

import About from "../pages/about.vue"
import Home from "../pages/home.vue"
import News from "../pages/News.vue"
import Message from "../pages/Message.vue"

Vue.use(VueRouter)

export default new VueRouter({
    // 配置n个路由
    // 注意是route 不是 router
    routes: [
        {
            path: "/about",
            component: About
        },
        {
            path: "/home",
            component: Home,
            // children用于配置子路由组件
            children:[
                {
                    path: "news",
                    component: News
                },
                {
                    path: "message",
                    component: Message
                }

            ]
        },
        {
            path: "/",
            redirect: "/about"
        }
    ]
})