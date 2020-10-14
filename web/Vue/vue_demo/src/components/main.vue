<template>
    <div>
        <h2 v-if="firstView">输入用户名搜索</h2>
        <h2 v-if="loading">Loading</h2>
        <h2 v-if="errorMsg">{{errorMsg}}</h2>
        <div class="row" v-for="(user, index) in users" :key="index">
            <div class="card" style="width: 100px">
                <a :href="user.url" target="_blank">
                    <img src="https://avatars.githubusercontent.com/u/6412038?v=3" alt="">
                </a>
                <p class="card-text">reactjs</p>
            </div>
           
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            firstView: true,
            loading: false,
            users: null,
            errorMsg: ""

        }
    }
    
}
</script>

<style>
.card{
    float: left;
    width: 33.333%;
    padding: .75rem;
    margin-bottom: 2rem;
    border: 1px solid #efefef;
    text-align: center;
}

.card img{
    width: 50%;
    margin-bottom: .75rem;
    border-radius: 100px;
}
.card-text{
    font-size: 85%
}

</style>