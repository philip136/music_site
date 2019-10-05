<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password" type="password" placeholder="Пароль"/>
        <button @click="setLogin">Войти</button>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    type: "POST",
                    url: "http://127.0.0.1:8000/api-token-auth/",
                    crossDomain: true,
                    dataType: "jsonp",
                    success: (response) => {
                        console.log(response)
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Login or password incorrect")
                        }
                    }
                })
            },
        }
    }
</script>

<style>
</style>
