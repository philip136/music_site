var $csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$(document).ready(function() {
    $('#edit').on('submit', function(event){
        event.preventDefault();
        let comment_id = $('#comment_id').val();
        $.ajax({
            type: 'PUT',
            url: 'http://localhost:8000/api/albums/' + comment_id + '/edit/',
            headers: {"X-CSRFToken": $csrf_token},
            data: {
                'post': $('.input_Text_post').val(),
                'text': $('.input_Text_text').val(),
            },
            success: function(data){
                console.log(data);
            }
        });
    });
});
