<template>
    <div>
        <h2> Chat </h2>
        <button @click goLogin> Login </button>
    </div>
</template>

<script>
    export default{
        name: 'Home',
        methods: {
            goLogin(){
                this.$router.push({name: "login"})
            },
        },
    }
</script>
