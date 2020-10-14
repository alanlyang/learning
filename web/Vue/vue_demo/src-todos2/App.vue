<template>
    <div class="todo-container">
        <div class="todo-wraper">
            <!-- 通过传方法的形式实现 -->
            <!-- <TodoHeader :addTodo="addTodo"/> -->
            <!-- 通过事件监听的形式实现 -->
            <!-- <TodoHeader @addTodo="addTodo"/> 给 TodoHeader绑定 addTodo的事件监听 -->
            <!-- 还可以通过Mounted生命周期来进行绑定 -->
            <TodoHeader ref="header"/>
            <TodoList :todos="todos" :deleteTodo="deleteTodo"/>
            <!-- <TodoFooter :todos="todos" :selectAllTodos="selectAllTodos" :deleteCompleteTodos="deleteCompleteTodos"/> -->
            <!-- 使用pubsub来进行消息订阅实现 -->
            <TodoFooter :todos="todos" :selectAllTodos="selectAllTodos" :deleteCompleteTodos="deleteCompleteTodos"/>
        </div>
    </div>
</template>

<script>
import storageUtil from "./util/storageUtil"
import PubSub from "pubsub-js"
import TodoHeader from "./components/TodoHeader.vue"
import TodoList from "./components/TodoList.vue"
import TodoFooter from "./components/TodoFooter.vue"

export default {
    data(){
        return {
            // todos: [
            //     {title: "吃放", complete: false},
            //     {title: "睡觉", complete: true},
            //     {title: "写代码", complete: false},
            // ]
            
            // 从LocalStorage中读取todos
            // 一旦todos发生了变化就进行存储,(需要进行深度监视)

            // window.localStorage可以进行数据的本地缓存
            todos: storageUtil.readTodos()


        }
    },
    mounted(){
        // 主要用来绑定一些异步代码
        // 给TodoHeaders绑定addTodo事件监听
        // this.$on('addTodo', this.addTodo) // 这样写是给app绑定的监听
        this.$refs.header.$on('addTodo', this.addTodo)

        // 订阅消息
        PubSub.subscribe("deleteTodo", (msg, index)=>{
            this.deleteTodo(index)

        })

    },
    components: {
        TodoFooter,
        TodoList,
        TodoHeader
    },
    methods:{
        addTodo(todo){
            this.todos.unshift(todo)
        },
        deleteTodo(index){
            this.todos.splice(index, 1)
        },
        deleteCompleteTodos(){
            // 删除所有选中的todos，是否选中由complete参数决定
            // 留下所有为false的todo
            this.todos = this.todos.filter(todo => !todo.complete)

        },
        selectAllTodos(check){
            // 全选/全不选
            // check 为最下面的checkbox是否选中
            this.todos.forEach(todo => todo.complete = check)
        }
    },

    watch : {
        todos: {
            deep: true,// 深度监视
            // 回调函数, 当监视的属性发生变化时，回调函数就会执行
            handler(value) {
                // 将todos最新的值保存到localStorage中, 需要存储为字符串，即转化为JSON类型的数据
                storageUtil.saveTodos(value)
            }
            // 也可以写成 handler : storageUtil.saveTodos
        }
    }
}
</script>

<style>
  .todo-wraper{
      width: 500px;
      margin: 50px auto;     
      border: 1px black solid;
  }

</style>