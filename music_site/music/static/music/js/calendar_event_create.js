$(document).ready(function(){
    initModal();
    setupStartEvent();
});

// better use HashMap
var monthsYear = {
    "January": '01',
    "February": '02',
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12',
}

var date = $(".month").text();
var month = date.split(" ")[0];
var year = date.split(" ")[1];
var current_date = monthsYear[month] + "." + year;
var setNewDate = document.getElementById("start-event");


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

// setup start event day
function setupStartEvent(){
    $(".event").click(function(event){
        let startEventDay = event.target.innerText;
        if (startEventDay < 10){
            startEventDay = "0" + startEventDay;
        }
        let full_date = startEventDay = startEventDay + "." + current_date;
        return full_date;
    })
}

// setup finish day event
function setupFinishEvent(){
    $(".event").click(function(event){
        let finishEventDay = event.target.innerText;
        return finishEventDay;
    })
}


// for post form
function getCalendarApiJson(){
  $(".btn_create").on("click", function(){
        $(".calendar_event_create").on("submit", function(event){
        event.preventDefault();
        let start_event = new Date("2020.01.01");
        let end_event = new Date("2020.01.02");
        console.log(start_event);
        let modal = document.getElementById("popup");
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/calendar/api/create/',
            dataType: "json",
            contentType: false,
            processData: false,
            headers: {"X-CSRFToken": $("#calendar_api_create input[name='csrfmiddlewaretoken']").val()},
            data: {
                'title': $("#title").val(),
                'start_event': start_event,
                'end_event': end_event,
                'notes': $("#notes").val(),
                'user': $('#user').val(),
            }.serialize(),
            success: function(data){
                alert("success");
                console.log("good");
            },
        });
    });
  });
}
