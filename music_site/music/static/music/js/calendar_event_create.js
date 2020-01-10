$(document).ready(function(){
    initModal();
});


function initModal(){
    $(document).delegate(".event", "click", function() { showModalEvent();});
}

// show modal
function showModalEvent(){
    let modal = document.getElementById("popup");
    let event = document.getElementsByClassName("event")
    $(event).on("click", function(){
       $(modal).modal("toggle");
    });
}

// for post form
function getCalendarApiJson(){
    $('#calendar_api_create').on('submit', function(event){
        let modal = document.getElementById("popup");
        let data = {
            title: modal.find('#calendar_api_create input[name="title"]').value,
            notes: modal.find('#calendar_api_create input[name="notes"]').value,
            start_event: modal.find('#calendar_api_create input[name="start_event"]').value,
            end_event: modal.find('#calendar_api_create input[name="end_event"]').value,
            user: modal.find("#calendar_api_create input[name='user']").value,
        };
        console.log(data);
        $.ajax({
            type: 'POST',
            url: '/calendar/api/create',
            dataType: "json",
            contentType: "application/json",
            headers: {"X-CSRFToken": $("#calendar_api_create input[name='csrfmiddlewaretoken']").val()},
            data: {
                "title": data['title'],
                "start_event": data['start_event'],
                "end_event": data['end_event'],
                "notes": data['notes'],
                "user": data['user'],
                },
            success: function(data){
                alert("success");
                console.log("good");
                $(".modal").modal("hide");

            },
            error: function(data){
                console.log(data);
                alert("error");
            }
        });
    });
}
