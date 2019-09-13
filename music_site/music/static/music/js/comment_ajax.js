
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


$('.input_Text_text').hide();
$('.input_Text_post').hide();
var $csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$(document).ready(function() {
    $(".button_edit").click(function(){
        var comment_id = ($(this).attr('value'));
        var $this = $(this);
        $this.toggleClass('button_edit');
        if ($this.hasClass('button_edit')){
            $this.text('Send comment');
        }
        else {
            $this.text('Change comment');
        }

        $('.input_Text_text').show();
        $('.input_Text_post').show();
        $('.comment_text').text($('.input_Text_post').val());
        $('.comment_text').text($('.input_Text_text').val());

        $('#edit').on('submit', function(event){
            event.preventDefault();
            $.ajax({
                type: 'PUT',
                url: 'http://localhost:8000/api/albums/' + comment_id + '/edit/',
                headers: {"X-CSRFToken": $csrf_token},
                data: {
                    'post': $('#input_Text_post').val(),
                    'text': $('#input_Text_text').val(),
                },
                success: function(data){
                    console.log(data);
                }
            });
        });
    });
});

