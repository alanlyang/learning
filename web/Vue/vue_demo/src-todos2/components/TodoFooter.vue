<template>
    <div class="todo-footer">
        <!-- 全选的操作 -->
        <label>
            <input type="checkbox" v-model="isAllCheck">
        </label>
        <!-- 显示需要动态显示 -->
        <span>已完成{{completeSize}}</span>/全部{{todos.length}}
        <!-- 删除的操作 -->
        <button class="btn-delete" v-show="completeSize" @click="deleteCompleteTodos">清除已完成任务</button>
    </div>
</template>

<script>
export default {
    props: {
        todos: Array, // 通过todo中的compelete可以判断是否完成
        // deleteCompleteTodos: Function, // 用来执行点击清除按钮时的操作
        selectAllTodos: Function // 用来进行全选的操作
    },
    computed: {
        completeSize(){
            return this.todos.reduce((preTotal, todo) => preTotal + (todo.complete?1:0), 0)
        },
        isAllCheck: {
            // 获取状态
            get(){
                return (this.completeSize === this.todos.length) && this.todos.length > 0
            },
            // 对todos进行勾选设置
            set(value){
                // value是当前Checkbox的最新值
                this.selectAllTodos(value)
            },
        }
    }
    
}
</script>

<style>
    .btn-delete{
        float: right;
        background-color: red;
    }


</style>