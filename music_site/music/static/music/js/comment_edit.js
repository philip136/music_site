var $csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');


$('#form-edit-save').on('click', function(event){
    event.preventDefault();
    $('#modalComments').modal('toggle');
    let comment_id = $('#comment_id').val();
    $.ajax({
        type: 'PUT',
        url: 'http://localhost:8000/api/albums/' + comment_id + '/edit/',
        headers: {"X-CSRFToken": $csrf_token},
        data: {
            'post': $('#input_Text_post').val(),
            'text': $('#input_Text_text').val(),
        },
        success: function(data){
            document.getElementById("comment_text").innerHTML=data.text;
        }
    });
});
