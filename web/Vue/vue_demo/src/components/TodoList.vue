<template>
  <ul class="todo-main">
      <TodoItem v-for="(todo, index) in todos" :key="index" :todo="todo" :index="index"/>
  </ul>
</template>

<script>
import TodoItem from "./TodoItem.vue"

export default {
    props: {
        todos: Array
    },
    components: {
        TodoItem
    }
}
</script>

<style>
    .todo-main{
        border: 1px black solid;
        border-left: 0px;
        border-right: 0px;
        border-radius: 2px;
    }

    li {
        list-style: none;
        height: 36px;
        line-height: 36px;
        padding: 0 5px;
        border-bottom: 1px solid #ddd;
    }

    .btn-danger{
        /* display: none; */
        float: right;
    }
</style>