$(document).ready(function(){
    initModalProfileEdit();
});

function initModalProfileEdit(){
    $(document).delegate("span", "click", function(event){
        event.preventDefault();
        showModalProfile();
    });
}

function showModalProfile(){
    let modal_edit = document.getElementById("popup");
    let form = document.getElementById("profile-edit");
    $(".edit_profile").on("click", function(){
        $(modal_edit).modal("show");
    });
};