<template>
    <mt-button type="primary" @click="handlerClick" class="col-sm-2">Important</mt-button>
</template>

<script>
import {Toast} from "mint-ui"
export default {
    methods:{
        handlerClick(){
            Toast("这里是Button的回调函数")

        }
    }

}
</script>

<style>

</style>