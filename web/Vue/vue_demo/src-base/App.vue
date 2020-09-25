<template>
    <div class="content">
        <img src="./assets/logo.png" alt="logo" class="logo">
         <!-- 使用组件 -->
        <HelloWorld/>
    </div>
</template>

<script>
// 引入组件
import HelloWorld from './components/HelloWorld.vue'
export default {
    //注册组件
    components: {
        HelloWorld: HelloWorld
    }
}
</script>

<style>
    .content{
        margin: 50px 0px;
    }
    .logo{
        width: 200px;
        height: 200px;
        background-color: salmon;
    }
</style>