<template>
    <div class="todo-container">
        <div class="todo-wraper">
            <TodoHeader :addTodo="addTodo"/>
            <TodoList :todos="todos" :deleteTodo="deleteTodo"/>
            <TodoFooter :todos="todos" :selectAllTodos="selectAllTodos" :deleteCompleteTodos="deleteCompleteTodos"/>
        </div>
    </div>
</template>

<script>
import TodoHeader from "./components/TodoHeader.vue"
import TodoList from "./components/TodoList.vue"
import TodoFooter from "./components/TodoFooter.vue"

export default {
    data(){
        return {
            todos: [
                {title: "吃放", complete: false},
                {title: "睡觉", complete: true},
                {title: "写代码", complete: false},
            ]
        }
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