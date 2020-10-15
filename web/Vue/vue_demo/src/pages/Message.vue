<template>
    <div>
        <ul>
            <li v-for="(message) in message_list" :key="message.id">
                <a href="???/">{{ message.title }}</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    data(){
        return{
            // 这里我们从后台获取数据
            message_list: []
        }
    },
    mounted(){
        // 模拟从后台获取数据
        setTimeout(()=>{
            const message_list = [
                {
                    title: "message01",
                    id: 1
                },
                {
                    title: "message02",
                    id: 2
                },
                {
                    title: "message03",
                    id: 3
                }
            ]
        },1000)

    }
    
}
</script>

<style>

</style>