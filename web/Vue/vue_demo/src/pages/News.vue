<template>
    <div>
        <ul>
            <li v-for="(news, index) in news_list" :key="index">{{ news.title }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data(){
        return{
            news_list: [
                {title: "news1", link: ""},
                {title: "news2", link: ""},
                {title: "news3", link: ""},
            ]
        }
    }
    
}
</script>

<style>

</style>