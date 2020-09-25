<template>
    <div>
        <p class="msg"> {{ msg }} </p> 
    </div>
</template>

<script>
export default {
    data(){
        return {
            msg: "Alan is a smart boy"
        }
    }
}
</script>

<style>
    .msg{
        font-size: 20px;
        color: red;
        width: 200px;
        height: 200px;
        background-color: #bbffaa;
    }

</style>