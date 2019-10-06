<template>
    <div>
        <h2> Chat Users </h2>
        <button v-if="!auth" @click="goLogin"> Login</button>
        <button v-else @click="logOut"> Log out </button>
        <Room v-if="auth"></Room>
    </div>
</template>

<script>
    import Room from '@/components/Room.vue'

    export default {
        name: 'Home',
        components:{
            Room
        },
        computed: {
            auth(){
                if (sessionStorage.getItem('auth_token')){
                    return true
                }
            }
        },
        methods: {
            goLogin(){
                this.$router.push({name: 'login'})
            },
            logOut(){
                sessionStorage.removeItem('auth_token')
                window.location = '/'
            }
        },
    }
</script>

<style scoped>

</style>