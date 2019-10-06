
$(document).ready(function(){
    $('.btn_create').on('click', function(){
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
                        // Need create your allert
                        alert('Comment created');
                        window.location.reload();
                    },
                    eror: function(data){
                        // Add erors handler for Not Auth
                    }
            });
        });
    });
});



