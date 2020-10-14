<template>
    <div>
        <div v-if="!repoUrl">loading</div>
        <div v-else>the most popular repo is <a :href="repoUrl">{{repoName}}</a></div>
    </div>
    
</template>

<script>
import axios from "axios"
export default {
    data(){
        return{
            repoUrl: "",
            repoName: ""
        }
    },
    mounted() {
        // 发送ajax来获取数据
        // 这里使用gitHub提供的api来进行测试 
        // https://api.github.com/search/repositories?
        const url =`https://api.github.com/search/repositories?q=DNN&sort=stars` // 模板字符串
        // this.$http.get(url).then(
        //     // 成功的回调函数
        //     response => {
        //         const result = response.data
        //         // 得到最受换欢迎的repo
        //         const mostRepo = result.items[0]
        //         this.repoUrl = mostRepo.html_url
        //         this.repoName = mostRepo.name
        //     },
        //     reponse => {
        //         alert("请求失败")
        //     }
        // )

        // 使用axios 发送 ajax请求
        axios.get(url).then(
             response => {
                const result = response.data
                // 得到最受换欢迎的repo
                const mostRepo = result.items[0]
                this.repoUrl = mostRepo.html_url
                this.repoName = mostRepo.name
            }
        ).catch(
            error=>{
                alert("我是真的请求失败了啊，哥")
            }
        )
    }
    
}
</script>

<style>
</style>