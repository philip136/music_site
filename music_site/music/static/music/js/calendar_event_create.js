$(document).ready(function(){
    initModal();
});


var modalIsActive = false;

function initModal(){
    $(document).delegate(".event", "click", function() { showModalEvent();});
    $(document).delegate("#save", "click", function() { getCalendarApiJson();});
}

// show modal
function showModalEvent(){
    let modal = document.getElementById("popup");
    let event = document.getElementsByClassName("event")
    $(event).on("click", function(){
       $(modal).modal("toggle");
       modalIsActive = true;
    });
}

// for post form
function getCalendarApiJson(){
        $('#create_event').on('submit', function(event){
            $.ajax({
                type: 'POST',
                url: 'http://localhost:8000/calendar/api/create',
                data: {
                    "title": $("#event-title").val(),
                    "start_event": $("#event-start").val(),
                    "end_event": $("#event-end").val(),
                    "notes": $("#event-notes").val(),
                    "user": $("#event-author").val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
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
