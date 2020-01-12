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

function action(data){
    console.log(data);
}

// for post form
function getCalendarApiJson(){
  $(".btn_create").on("click", function(){
    $('#calendar_api_create').on('submit', function(event){
        let modal = document.getElementById("popup");
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/calendar/api/create/',
            dataType: "json",
            headers: {"X-CSRFToken": $("#calendar_api_create input[name='csrfmiddlewaretoken']").val()},
            data: {
                'title': $("#title").val(),
                'start_event': $("#start_event").val(),
                'end_event': $("#end_event").val(),
                'notes': $("#notes").val(),
                'user': $('#user').val(),
            },
            success: function(data){
                alert("success");
                console.log("good");
                $(".modal").modal("hide");

            },
            error: function(data){
                action(data);
                alert("error");
            }
        });
    });
  });
}
