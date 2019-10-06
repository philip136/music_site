<template>
    <div class=dialog>
        <div v-for="dialog in dialogs">
            <h3>{{dialog.user.username}}</h3>
            <p>{{dialog.text}}</p>
            <span>{{dialog.date}}</span>
        </div>
    </div>
    
</template>

<script>
import $ from 'jquery'

export default {
    name: 'Dialog',
    props: {
        id: '',
    },
    data(){
        return {
            dialogs: '',
        }
    },
    created(){
        $.ajaxSetup({
            headers: {"Authorization": "Bearer " + sessionStorage.getItem('auth_token')},
        });
        this.loadDialog()
    },
    methods: {
        loadDialog(){
            $.ajax({
                url: 'http://127.0.0.1:8000/api/chat/dialog/?room=',
                type: "GET",
                data:{
                    room: this.id,
                },
                success: (response) => {
                    this.dialogs = response.data
                    console.log(response.data)
                }
            })
        }
    }
}
</script>

<style scoped>
    .dialog{
        width:70%;
        height:140px;
        border: 1px solid #000;
    }
</style>