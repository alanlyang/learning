<template>
  <li>
    <label>
      <input type="checkbox" v-model="todo.complete"/>
      <span :class="isDelete">{{ todo.title }}</span>
    </label>
    <button class="btn btn-danger">删除</button>
  </li>
</template>

<script>
export default {
    props:{
        todo: Object,
        index: Number
    },

    data(){
        return {
            isDelete: ""
        }
    },

    methods:{
        checkItem(){
            const complete = this.todo.complete
            if (!complete){
                this.isDelete = 'bClass'
            }
            else{
                this.isDelete = "aClass"
            }
        }
    }
    
}
</script>

<style>
    li {
        list-style: none;
        height: 36px;
        line-height: 36px;
        padding: 0 5px;
        border-bottom: 1px solid #ddd;
    }

    .btn-danger {
        display: none;
    }

    li:hover .btn-danger{
        display: inline-flex;
        float: right;
        
    }

    .aClass {
        text-decoration: line-through;
    }

    .bClass {
        text-decoration: none;
    }

</style>