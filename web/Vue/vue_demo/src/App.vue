<template>
    <div>
        <div class="row">
            <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header">
                    <h2>Router Basic</h2>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-xs-offset-2">
                <div class="list-group">
                    <router-link to="/about" class="list-group-item">About</router-link>
                    <router-link to="/home" class="list-group-item">Home</router-link>
                </div>
            </div>
            <div class="col-xs-6">
                <div class="pannel">
                    <div class="pannal-body">
                        <keep-alive>
                        <router-view></router-view>
                        </keep-alive>
                        <!-- <router-view></router-view> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted(){
        this.$route.push({
            name: "home",
            params: {
                msg: "这是home的参数"
            }

        })
    }
}
</script>

<style>

</style>