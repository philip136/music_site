<template>
    <div>
        <ul>
            <li v-for="room in rooms">
                <h3>{{room.creater.username}}</h3>
                {{room.date}}
            </li>
        </ul>
    </div>
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
                    console.log(response)
                }
            })
        }
    },
}
</script>

<style scoped>

</style>