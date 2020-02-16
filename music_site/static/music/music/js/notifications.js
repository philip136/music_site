$(document).ready(function(){
    var modal_notify = $("#notifications").modal({
        show: false
    });

    // open modal window
    $("#notification-alert").on("click", function(){
        $(modal_notify).modal("show");
    });
    var message_notification = date_diff();
    setup_date_in_div(message_notification);

});
// for js date
var months = {
    "Jan": 0,
    "Feb": 1,
    "Mar": 2,
    "Apr": 3,
    "May": 4,
    "Jun": 5,
    "Jul": 6,
    "Aug": 7,
    "Sep": 8,
    "Oct": 9,
    "Nov": 10,
    "Dec": 11,
}
//for js date
var js_date = function convertDateJs(){
    js_date = new Date();
    return js_date;
};

// for python date
var python_date = function convertDatePy(){
    date = document.getElementById("time-to-finish").getAttribute("data-notify").trim();
    month = months[date.split(" ")[0].slice(0,3)];
    digit = date.split(" ")[1].slice(0,2);
    year = date.split(" ")[2].slice(0,4);
    hour = (date.split(" ")[3]).split(":")[0]
    minute = (date.split(" ")[3]).split(":")[1]
    let python_date = new Date(year,month,digit,hour,minute);
    return python_date;
};
// difference between end_event and date now
var date_diff = function getNewDate(){
    millisec_diff = python_date() - js_date();

    days = Math.floor(millisec_diff/1000/60/(60*24));
    let date_diff = new Date(millisec_diff);
    return days + " Days "+ date_diff.getHours() + " Hours " + date_diff.getMinutes() + " Minutes";
}

var setup_date_in_div = function setupRemainingDate(date){
    div = document.getElementById("time-to-finish").innerHTML = date;
}