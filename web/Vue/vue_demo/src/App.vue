<template>
    <div class="todo-container">
        <div class="todo-wraper">
            <TodoHeader/>
            <TodoList :todos="todos"/>
            <TodoFooter/>
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
                {title: "睡觉", complete: false},
                {title: "写代码", complete: false},
            ]
        }
    },
    components: {
        TodoFooter,
        TodoList,
        TodoHeader
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