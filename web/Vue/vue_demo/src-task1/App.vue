<template>
  <div>
    <header class="site-header jumbotron">
      <div class="container">
        <div class="row">
          <div class="col-xs-12">
            <h1>请发表对Alan的评论</h1>
          </div>
        </div>
      </div>
    </header>

    <div class="container">
      <Add :addComment="addComment" />
      <!-- 需要将数据传递到List组件, 加:是为了表示传递的是一个变量， -->
      <List :comments="comments" :deleteComment="deleteComment"/>
    </div>
  </div>
</template>

<script>
import Add from "./components/Add.vue";
import List from "./components/List.vue";
export default {
  //绑定数据 需要绑定 名称：类型
  // 在哪里进行绑定主要取决于这些数据在哪里使用，如果多个组件都需要使用，则需要在他们的父组件声明

  // 组件中的数据必须用函数的形式声明
  data() {
    return {
      // 数据在哪个组件，更新数据的行为(方法)就应该在哪个组件
      comments: [
        {
          name: "A",
          comment: "Right",
        },
        {
          name: "B",
          comment: "Agree",
        },
        {
          name: "C",
          comment: "Total Agree",
        },
      ],
    };
  },
  methods: {
    // 添加评论
    addComment(comment) {
      this.comments.unshift(comment);
    },
    // 删除指定下标的评论
    deleteComment(index){
        this.comments.splice(index,1)
    }
  },
  components: {
    Add,
    List,
  },
};
</script>

<style>
</style>
