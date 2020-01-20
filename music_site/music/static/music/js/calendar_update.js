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
    // delegate
    initModalEventEdit();
});

function initModalEventEdit(){
    $(document).delegate("#event-edit", "click", function(event) {
        event.preventDefault();
        showModalEvent();
    });
};

function showModalEvent(){
    let modal = document.getElementById("popup");
    $(modal).modal("show");
    let form = document.getElementById("post-form");
    let title = document.getElementById("event-edit").getAttribute("data-title")
    let start_event = document.getElementById("event-edit").getAttribute("data-start");
    let end_event = document.getElementById("event-edit").getAttribute("data-end");
    let notes= document.getElementById("event-edit").getAttribute("data-notes");
    let user = document.getElementById("event-edit").getAttribute("data-user");

    let e_title = document.getElementById("block-title").value = title;
    let e_start_event = document.getElementById("block-start").value = start_event;
    let e_end_event = document.getElementById("block-end").value = end_event;
    let e_notes = document.getElementById("block-notes").value = notes;
    let e_user = document.getElementById("block-user").value = user

    initForm(form, "title", e_title);
    initForm(form, "start_event", e_start_event);
    initForm(form, "end_event", e_end_event);
    initForm(form, "notes", e_notes);
    initForm(form, "user", e_user);
    form.action = "/calendar/event-update/" + document.getElementById("event-edit").getAttribute("data-id") + "/";
}

function initForm(formId, elementName, initText){
    let formElem = formId.elements[elementName];
    formElem.value = initText;
    return formElem;
}