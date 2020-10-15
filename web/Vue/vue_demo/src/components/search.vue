<template>
    <section class="jumbotron">
        <h3 jumbotron-heading>Search Github Users</h3>
        <div>
            <input type="text" class="col-sm-3" placeholder="enter the name you want to search" v-model="searchName">
            <button @click="search">search</button>
        </div>

    </section>
    
</template>

<script>
import PubSub from "Pubsub-js"

export default {
    data(){
        return {
            searchName: ""
        }
    },

    methods:{
        search(){
            const searchName = this.search.trim()
            if(searchName){
                // 发布search消息
                PobSub.publish("search", searchName)
            }
        }
    }
    
}
</script>

<style>

</style>