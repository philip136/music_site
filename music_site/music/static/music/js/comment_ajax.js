$('.leave_comment').click(function(){
    $.ajax({
        url: "http://localhost:8000/api/albums/create/",
        dataType: "json",
        success: function(data){
            $('#username').text(data[0].author);
            $('#comment').text(data[0].text);
        }
    });
});

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
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data){
                console.log(data);
        }
    });
});