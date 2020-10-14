<template>
<!--
    1、onmouseenter
    2、onmouseover 
    3、onmouseleave
    4、onmouseout

    over和out在进入内部元素的时候也会触发
    enter和leave进入子元素不会触发
 -->
  <li @mouseenter="handleShow(true)" @mouseleave="handleShow(false)" :style="{background: bgColor}">
    <label>
      <input type="checkbox" v-model="todo.complete"/>
      <span>{{ todo.title }}</span>
    </label>
    <button class="btn btn-danger" v-show="isShow" @click="deleteItem">删除</button>
  </li>
</template>

<script>
import PubSub from "pubsub-js"
export default {
    props:{
        todo: Object,
        index: Number,
        deleteTodo: Function
    },

    data(){
        return {
            bgColor: 'white', // 默认背景颜色
            isShow: false, //按钮默认是否显示,

            // state: todo.complete
        }
    },

    methods:{
        handleShow(isEnter){
            console.log(isEnter)
            if(isEnter){
                this.bgColor = "#aaaaaa"
                this.isShow = true
            }
            else{
                this.bgColor = 'white'
                this.isShow = false
            }
        },
        deleteItem(){
            const {todo,index} = this
            if(window.confirm(`确认删除${todo.title}么？`)){
                // this.deleteTodo(index)
                // 发布消息
                PubSub.publish("deleteTodo", index)
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
    .btn {
        float: right;
    }

    /* .btn-danger {
        display: none;
    } */

    /* li:hover .btn-danger{
        display: inline-flex;
        float: right;
        
    } */

    .aClass {
        text-decoration: line-through;
    }

    .bClass {
        text-decoration: none;
    }

</style>