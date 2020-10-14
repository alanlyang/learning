<template>
    <div class="container">
        <Search/>
        <UsersMain/>
    </div>
</template>

<script>
import Search from "./components/search.vue"
import Main from "./components/main.vue"
export default {
    components: {
        Search,
        UsersMain: Main
    },

    data(){
        return
    }
}
</script>

<style>

</style>