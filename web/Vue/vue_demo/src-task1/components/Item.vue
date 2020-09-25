<template>
  <li class="list-group-item">
    <div class="handle">
      <a href="javascript:;" @click="deleteItem">删除</a>
    </div>
    <p class="user">
      <span>{{ comment.name }}</span><span>说:</span>
    </p>
    <p class="sentence">{{ comment.comment }}</p>
  </li>
</template>

<script>
export default {
    // 声明接受属性，属性会成为组件对象的属性
    props: { // 指定属性名和属性值
        // 将comment声明为对象
        comment: Object,
        deleteComment: Function,
        index: Number
    },
    methods:{
        deleteItem(){
            const {comment, index, deleteComment} = this
            if(window.confirm(`确定要删除${comment.name}的评论么？`)){
                deleteComment(index)
            }
        }
    }
};
</script>

<style>
   li{
        transition: .5s;
        overflow: hidden;
    }

    .handle{
        width: 40px;
        border: 1px, solid, #cccccc;
        background-color: #fff;
        position: absolute;
        right: 10px;
        top: 1px;
        text-align: center;
    }

    .handle a{
        display: block;
        text-decoration: none;
    }

    .list-group-item .sentence{
        padding: 0px 50px;
    }

    .user{
        font-size: 22px;
    }

</style>
