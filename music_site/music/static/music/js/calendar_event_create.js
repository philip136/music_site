$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = $('[name=csrfmiddlewaretoken]').val();

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
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
};

// show modal
function showModalEvent(){
    let modal = document.getElementById("popup");
    let event = document.getElementsByClassName("event")
    $(event).on("click", function(){
       $(modal).modal("toggle");
       $("#post-form").on("submit", function(event){
            event.preventDefault();
            create_event();
        });
    });
};

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

function create_event(){
    console.log("create event");
    $.ajax({
        type: "POST",
        data: {
            'title': $("#title").val(),
            'start_event': $("#start_event").val(),
            'end_event': $("#end_event").val(),
            'notes': $("#notes").val(),
            'user': $("#user").val(),
        },
        cache: true,
        success: function(json){
            alert("success");
            document.getElementById("post-form").reset();
        },
        error: function(xhr, error_msg, err){
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};

