<template>
    <div class="col-md-8">
        <h3 class="reply">评论回复</h3>
        <h2 v-show="comments.length===0">暂无评论，点击添加评论</h2>
        <ul class="list-group">
            <Item v-for="(comment, index) in comments" :key="index" :comment="comment"  :deleteComment="deleteComment" :index="index"/>
        </ul>
    </div>
</template>

<script>
import Item from "./Item.vue"
export default {
    // 声明接受属性，这个属性就会成为组件对象的属性
    props: ['comments', "deleteComment"],
    components:{
        Item
    }
    
}
</script>

<style>
    /* h2{
        display: none;
    } */
    .reply{
        margin-top: 0px
    }

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
