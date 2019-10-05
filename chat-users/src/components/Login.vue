<template>
    <div>
        <input v-model="login" type="text" placeholder="login">
        <input v-model="password" type="password" placeholder="password">
        <button @click="setLogin"> Login </button>
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
                    url: "http://127.0.0.1:8000/api/token/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        console.log(response)
                    },
                    error: (response) => {
                        if (response.status === 401) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        }
    }
</script>