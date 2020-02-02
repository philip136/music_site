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
    showEventOnCalendar();
    
    // init day
    currentDayInit();
    // delegate
    initModal();
});

function* generatForEvents(count_events){
    for (let i=0; i<count_events.length; i++){
        yield count_events[i];
    }
}

// In here fill td elem if he exist event
function showEventOnCalendar(){
    let data_events = document.querySelectorAll("#event-edit");
    let count = 0;
    let generator = generatForEvents(data_events);
    elem = generator.next().value;
    data_title = elem.getAttribute("data-title");
    data_start = elem.getAttribute("data-start");
    data_end = elem.getAttribute("data-end").split(" ");
    data_notes = elem.getAttribute("data-notes");
    month = data_end[0].slice(0,3);
    day = data_end[1].slice(0,1);
    for (let size=0; size < data_events.length; size++){
        if (document.querySelector("th.month").innerText.slice(0,3) == month){
            td_elem = document.querySelectorAll("#event-field");
            search_text = day;
            let td_found = new Array();
            for (let i=0; i < td_elem.length; i++){
                if (td_elem[i].innerText == search_text){
                    td_found.push(td_elem[i]);
                }
            }
            for (let e = 0; e < td_found.length; e++){
                td_found[e].style.backgroundColor = "#2ECC71";
                td_found[e].style.color = "white";
                td_found[e].style.fontSize = "20px";
                td_found[e].style.align = "center";
                info_date = document.querySelector("#event-info-date");
                li_elem = document.createElement("li");
                li_elem.innerText = data_title + " - " + data_notes;
                info_date.appendChild(li_elem);
                count ++;
            }
        }
        if (count < data_events.length){
            elem = generator.next().value;
            data_title = elem.getAttribute("data-title");
            data_start = elem.getAttribute("data-start");
            data_end = elem.getAttribute("data-end").split(" ");
            data_notes = elem.getAttribute("data-notes");
            month = data_end[0].slice(0,3);
            day = data_end[1].slice(0,1);
        }
    }
}

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
    // open modal
    $(document).delegate("div", "click", function(event) {
        event.preventDefault();
        showModalEvent();
    });

    // create new event
    $(document).delegate("td", "click", function(event){
        event.preventDefault();
        initNewEvent();
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

// Setup date for event-start date
function setupDate(){
    var month_and_year = $(".month").text()
    var monthName = month_and_year.split(" ")[0];
    var monthNumber = monthDictionary[monthName];
    var year = month_and_year.split(" ")[1];
    var day = $("div.num-date").text();
    var date = new Date();
    var hour = new String(date.getHours());
    var minute = new String(date.getMinutes());
    if (hour.length < 2){hour = "0" + hour}
    if (minute.length < 2){minute = "0" + minute}

    if (day < 10){
        date = year + "-" + monthNumber + "-0" + day + "T" + hour + ":" + minute;
    }
    else if (day > 10){
        date = year + "-" + monthNumber + "-" + day + "T" + hour + ":" + minute;
    }
    return date;
};

function showModalEvent(){
    let modal = document.getElementById("popup");
    let setDate = setupDate();
    setStartEvent = document.getElementById("block-start");
    let date_start = setStartEvent.querySelector("input[name='start_event']");
    date_start.defaultValue = setDate;
    $(".add-event").click(function(event){
       event.preventDefault();
       $(modal).modal("show");
       $("#post-form").on("submit", function(){
            create_event();
        });
    });
    $(".create-event").click(function(event){
       event.preventDefault();
       $(modal).modal("show");
       $("#post-form").on("submit", function(){
            create_event();
        });
    });
};

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

