
$(document).ready(function(){
    $('#post_form').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/api/albums/create/',
            data: {
                'post': $('#post').val(),
                'text': $('#text').val(),
                'author': $('#author').val(),
                'album': $('#album').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data){
                    if (data.error === false){
                        $('#post_form').attr('validated',true);
                        $('#post_form').unbind().submit();
                    }
                    if (data.error === true){
                        alert('Error message');
                    }
            }
        });
    });
});



