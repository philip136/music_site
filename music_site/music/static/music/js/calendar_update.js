$(document).ready(function(){
    initModalEventEdit();
});

function initModalEventEdit(){
    $(document).delegate("span", "click", function(event) {
        event.preventDefault();
        showModalEventEdit();
    });
};

function showModalEventEdit(){
    let modal_edit = document.getElementById("modal-all-events");
    let form = document.getElementById("event-form-edit");
    // page with delete and edit buttons
    $(".posts").on("click", function(){
        $(modal_edit).modal("show");
        let btn_edit = document.querySelector("button#event-edit.btn.btn-success");
        $(btn_edit).on("click", function(){
            let modal_edit_event = document.getElementById("popup-for-edit");
            $(modal_edit_event).modal("show");
        });
    });
    // get all old fields value from button
    let title = document.getElementById("event-edit").getAttribute("data-title")
    let start_event = document.getElementById("event-edit").getAttribute("data-start");
    let end_event = document.getElementById("event-edit").getAttribute("data-end");
    let notes= document.getElementById("event-edit").getAttribute("data-notes");

    let e_title = document.getElementById("block-title-edit").value = title;
    let e_start_event = document.getElementById("block-start-edit").value = start_event;
    let e_end_event = document.getElementById("block-end-edit").value = end_event;
    let e_notes = document.getElementById("block-notes-edit").value = notes;

    initForm(form, "title", e_title);
    initForm(form, "start_event", e_start_event);
    initForm(form, "end_event", e_end_event);
    initForm(form, "notes", e_notes);
    form.action = "/calendar/event-update/" + document.getElementById("event-edit").getAttribute("data-id") + "/";
}

function initForm(formId, elementName, initText){
    let formElem = formId.elements[elementName];
    formElem.value = initText;
    return formElem;
}