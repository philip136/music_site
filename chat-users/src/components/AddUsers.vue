<template>
    <div>
        <select v-model="option">
            <option disabled value="">Please select user</option>
            <option v-for="user in list" :value="user.id">{{user.username}}</option>
            
        </select>
        <mu-button class="btn-send" round color="success" @click="addUser">Add User</mu-button>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    name: "AddUsers",
    props: {
        room: '',
    },
    data(){
        return {
            option: '',
            list: '',
        }
    },
    created(){
        this.loadUsers()
    },
    methods: {
        loadUsers(){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/chat/users_invited/',
                type: "GET",
                success: (response) => {
                        this.list = response
                }
            })
        },
        addUser(){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/chat/users_invited/',
                type: "POST",
                data: {
                    room: this.room,
                    user: parseInt(this.option),
                },
                success: (response) => {
                    alert('User added')
                },
                error: (response) => {
                    console.log(this.room, this.option)
                    alert('Error add user')
                }
            })

        }
    }
}
</script>

<style scoped>

</style>