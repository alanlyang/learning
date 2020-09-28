<template>
    <div class="todo-header">
        <h2>请输入你的待办:</h2>
        <input class="addTask" type="text" placeholder="输入任务名称,然后按回车键确认" />
    </div>
</template>

<script>
export default {
    
}
</script>

<style>
    .todo-header{
        /* border: 1px black solid; */
        margin-bottom: 5px;
        margin-left: 10px;
        /* height: 10px */
    }

    h2{
        font-size: 20px
    }

    .addTask{
        width: 80%
    }
    
    

</style>