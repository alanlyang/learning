<template>
    <div class="todo-header">
        <h2>请输入你的待办:</h2>
        <!-- 看到input就应该想到v-model -->
        <input class="addTask" type="text" placeholder="输入任务名称,然后按回车键确认" v-model="title" @keyup.enter="addItem"/>
    </div>
</template>

<script>
export default {
    props: {
        // addTodo: Function
    },
    data(){
        return {
            title: ""
        }
    },

    methods: {
        addItem(){
            // 检查输入的合法行
            const title = this.title.trim()

            if (!title){
                alert("必须输入")
                return
            }

            // 根据输入生成一个todo对象
            const todo = {
                title,
                complete: false
            }

            // 添加到todos(数据在哪里，更新数据的方法就在哪里定义)
            // this.addTodo(todo)
            // 触发自定义事件
            this.$emit('addTodo', todo)

            // 清除输入
            this.title = ""
        }
    }
    
}
</script>

<style>
    .todo-header{
        /* border: 1px black solid; */
        margin-bottom: 5px;
        margin-left: 10px;
        /* height: 10px */
    }

    h2{
        font-size: 20px
    }

    .addTask{
        width: 80%
    }
    
    

</style>