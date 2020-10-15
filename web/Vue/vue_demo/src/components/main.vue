<template>
    <div>
        <h2 v-if="firstView">输入用户名搜索</h2>
        <h2 v-if="loading">Loading</h2>
        <h2 v-if="errorMsg">{{errorMsg}}</h2>
        <div class="row" v-for="(user, index) in users" :key="index">
            <div class="card" style="width: 100px">
                <a :href="user.url" target="_blank">
                    <img :src="user.avatar_url" alt="">
                </a>
                <p class="card-text">reactjs</p>
            </div>
           
        </div>
    </div>
</template>

<script>

import PubSub from "Pubsub-js"
import axios from "axios"

export default {
    data(){
        return{
            firstView: true,
            loading: false,
            users: null, // [{url: "", avatar_url: "", name: ""}]
            errorMsg: ""

        }
    },

    /**
     * ajax选择写在main里是因为每次搜索都要更新main的数据，如果写在另一个组件中，则必须要进行组件间的通信
     * 因此写在数据更新的地方会比较好
     */
    mounted() {
        /**
         * 不能在Mounted中发请求
         * mounted是在实例初始化的时候进行请求发送
         * 而这里需要在点击search之后发送请求
         * 
         * 这里的通信是兄弟组件间的通信，因此最好通过消息订阅的形式来进行通信，即使用PobSub来进行
         * 监听 === 订阅事件
         * 触发 === 发布事件
         * 
         * 这里显然是在点击search按钮后进行触发，因此监听需要在当前组件监听
         * 触发需要在search组件中进行绑定
         */

        //订阅 search消息
        Pubsunstore.subscribe("search", (msg, searchName)=>{
            // 更新状态
            
            // 发送ajax请求
            const url = `https://api.github.com/search/users?q=${searchName}`
            axios.get(url)

        })


    },

    
}
</script>

<style>
.card{
    float: left;
    width: 33.333%;
    padding: .75rem;
    margin-bottom: 2rem;
    border: 1px solid #efefef;
    text-align: center;
}

.card img{
    width: 50%;
    margin-bottom: .75rem;
    border-radius: 100px;
}
.card-text{
    font-size: 85%
}

</style>