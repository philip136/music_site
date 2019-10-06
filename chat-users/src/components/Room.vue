<template>
    <mu-col span="4" xl="2" sm="4" class="rooms-list">
        <div v-for="room in rooms">
            <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
            <small>{{room.date}}</small>
        </div>
    </mu-col>
</template>

<script>
import $ from 'jquery'

export default {
    name: "Room",
    data(){
        return {
            rooms: '',
            
        }
    },
    created(){
        $.ajaxSetup({
            headers: {"Authorization": "Bearer " + sessionStorage.getItem('auth_token')},
        });
        this.loadRoom()
    },
    methods: {
        loadRoom(){
            $.ajax({
                url: "http://127.0.0.1:8000/api/chat/room/",
                type: "GET",
                success: (response) =>{
                    this.rooms = response.data
                }
            })
        },
        openDialog(id){
            this.$emit('openDialog', id)
        }
    },
}
</script>

<style scoped>
    h3{
        cursor: pointer;
    }
    .rooms-list{
        box-shadow: 1px 2px 3px #cccccc;
        margin: 10px;
    }
</style>