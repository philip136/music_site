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
                console.log(data);
        }
    });
});


