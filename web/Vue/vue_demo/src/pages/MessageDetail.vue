<template>
    <div>
        <p>ID: {{$route.params.id}}</p>
        <ul>
            <li>id: {{message_detail.id}}</li>
            <li>title: {{message_detail.title}}</li>
            <li>content: {{message_detail.content }}</li>
        </ul>
    </div>
</template>

<script>
export default {
   data(){
       return{
           // 从后台获取的消息详情页
           message_detail_list: [],
           message_detail: {}
       }
   },
   mounted() {
       // 模拟ajax请求
       setTimeout(()=>{
           const all_list = [
                {
                    title: "message01",
                    id: 1,
                    content: "message01 content ..."
                },
                {
                    title: "message02",
                    id: 2,
                    content: "message02 content ..."
                },
                {
                    title: "message03",
                    id: 3,
                    content: "message03 content ..."
                }
            ]
            
            this.message_detail_list = all_list
            // 写着这里的话Mounted只会执行一次，会导致数据异常
           
       }, 1000)
   },
   watch: {
       $route: function(value){
           // 这里的value其实就是路由路径
           const id = this.$route.params.id * 1
           this.message_detail = this.message_detail_list.find(detail=>detail.id === id)
       }
   }
    
}
</script>

<style>
</style>