var $csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$(document).ready(function(){
    $('.btn_del').click(function(){
        let comment_id = $('.btn_del').val();
        $.ajax({
            type: 'DELETE',
            url: 'http://localhost:8000/api/albums/' + comment_id + '/delete/',
            headers: {"X-CSRFToken": $csrf_token},
            success: function(data){
                console.log('comment success delete')
            }
        });
    });
});