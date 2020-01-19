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
    // init day
    currentDayInit();
    // delegate
    initModal();
});

var monthDictionary = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
};

var weekday = new Array(7);
weekday[0] = "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

var createBtn = false;
var todayNameDay = weekday[new Date().getDay()];
var todayDayDigit = new Date().getDate();
var abbrev_name = todayNameDay.slice(0,3);

abbrev_name = abbrev_name.toLowerCase();
$("."+abbrev_name).css({"color": "#2ECC71"});

function currentDayInit(){
    let elem_date = $("span.date").val(todayDayDigit)[todayDayDigit-1];
    if (elem_date.value == todayDayDigit){
        elem_date.className = "active-day";
    }
}

function initModal(){
    $(document).delegate("div.add-event", "click", function(event) {
        event.preventDefault();
        showModalEvent();
    });
    $(document).delegate("td", "click", function(event){
        event.preventDefault();
        initNewEvent();
    });
    $(document).delegate(".posts", "click", function(event){
        event.preventDefault();
        let modal = document.getElementById("modal-all-events");
        console.log("event");
        $(modal).modal("toggle");
    });
};

// Initialization new event after click number on calendar
function initNewEvent(){
    let day = event.target.innerText;
    let year = $('.month').text().split(" ")[1];
    let month_name = $('.month').text().split(" ")[0];
    let month = monthDictionary[month_name];
    let date = new Date(year,month-1,day);
    let abbreviated_name = weekday[date.getDay()].slice(0,3);
    abbreviated_name = abbreviated_name.toLowerCase();
    $(".num-date").text(day);
    $(".day").text(weekday[date.getDay()]);
}

function getAllEvents(event){
    var events = event.target.innerText;
    if (events.length > 0 && createBtn == false){
        var btn_del = document.createElement("BUTTON");
        btn_del.innerHTML = "Delete";
        btn_del.className += "btn btn-primary btn-xs btn_del"
        document.getElementById("title-event").appendChild(btn_del);
        createBtn = true;
    }
}


function setupDate(event){
    var month_and_year = $(".month").text()
    var monthName = month_and_year.split(" ")[0];
    var monthNumber = monthDictionary[monthName];
    var year = month_and_year.split(" ")[1];
    var day = $("div.num-date").text();
    var date = new Date();
    var time = date.getHours() + ":" + date.getMinutes();
    if (day < 10){
        date = year + "-" + monthNumber + "-0" + day + "T" + time;
    }
    else if (day > 10){
        date = year + "-" + monthNumber + "-" + day + "T" + time;
    }
    return date;
};

function showModalEvent(){
    let modal = document.getElementById("popup");
    $("div.add-event").click(function(event){
       event.preventDefault();
       let setDate = setupDate(event);
       let setStartEvent = document.getElementById("start_event");
       setStartEvent.defaultValue = setDate;
       $(modal).modal("toggle");
       $("#post-form").on("submit", function(){
            create_event(setStartEvent);
        });
    });
    $("div.create-event").click(function(event){
       event.preventDefault();
       let setDate = setupDate(event);
       let setStartEvent = document.getElementById("start_event");
       setStartEvent.defaultValue = setDate;
       $(modal).modal("toggle");
       $("#post-form").on("submit", function(){
            create_event(setStartEvent);
        });
    });
};

function create_event(start_time){
    console.log("create event");
    $.ajax({
        type: "POST",
        data: {
            'title': $("#title").val(),
            'start_event': document.getElementById("start_event").defaultValue,
            'end_event': $("#end_event").val(),
            'notes': $("#notes").val(),
            'user': $("#user").val(),
        },
        cache: true,
        success: function(response){
            if (response.status_code == 200){
                alert("success");
            }
            else {
                let r = document.getElementById("end_event");
                r.required = true;
                console.log("error");
            }
        },
        error: function(response){
            console.log(response);
        }
    });
};

