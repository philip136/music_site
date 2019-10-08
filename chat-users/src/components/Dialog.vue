<template>
    <mu-col span="8" xl="9">
        <AddUsers :room="id"></AddUsers>
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs" direction="column" justify-content="start" align-items="end">
                <h3>{{dialog.user.username}}</h3>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-text-field ref="textField" v-model="form.textarea" full-width placeholder="Please input message"/>
            <mu-button class="btn-send" round color="success" @click="sendMessage"> Send </mu-button>
        </mu-container> 
    </mu-col>
</template>

<script>
import $ from 'jquery'
import AddUsers from './AddUsers.vue'

export default {
    name: 'Dialog',
    props: {
        id: '',
    },
    components: {
        AddUsers
    },
    data(){
        return {
            dialogs: '',
            form: {
                textarea: '',
            }
        }
    },
    created(){
        $.ajaxSetup({
            headers: {"Authorization": "Bearer " + sessionStorage.getItem('auth_token')},
        });
        setInterval(() => {
            this.loadDialog()
        }, 5000)
    },
    methods: {
        loadDialog(){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/chat/dialog/',
                type: "GET",
                data:{
                    room: this.id,
                },
                success: (response) => {
                    this.dialogs = response.data
                }
            })
        },
        sendMessage(){
             $.ajax({
                url: 'http://127.0.0.1:8000/api/chat/dialog/?room=',
                type: "POST",
                data:{
                    room: this.id,
                    text: this.form.textarea,
                },
                success: (response) => {
                    this.loadDialog()
                },
                error: (response) => {
                    alert(response.statusText)
                },
            })
        }
    }
}
</script>

<style scoped>
    .dialog{
        border: 1px solid #000;
    }
    .btn-send{
        margin: -50px 0 0 15px;
    }
</style>