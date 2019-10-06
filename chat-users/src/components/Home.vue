<template>
    <div>
        <h2> Chat Users </h2>
        <button v-if="!auth" @click="goLogin"> Login</button>
        <button v-else @click="logOut"> Log out </button>
        <Room v-if="auth" @openDialog="openDialog"></Room>
        <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </div>
</template>

<script>
    import Room from '@/components/Room.vue'
    import Dialog from '@/components/Dialog.vue'

    export default {
        name: 'Home',
        components:{
            Room,
            Dialog
        },
        data(){
            return {
                dialog:{
                    id: '',
                    show: false,
                }
            }
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
            },
            openDialog(id){
                this.dialog.id = id
                this.dialog.show = true
            }
        },
    }
</script>

<style scoped>

</style>