<template>
  <ul class="todo-main">
      <TodoItem v-for="(todo, index) in todos" :key="index" :todo="todo" :index="index" />
  </ul>
</template>

<script>
import TodoItem from "./TodoItem.vue"

export default {
    props: {
        todos: Array,
        // deleteTodo: Function
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

</style>