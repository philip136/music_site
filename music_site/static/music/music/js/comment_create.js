function closeAlert(){
    $('.btn-close').on('click',function(){
        window.location.reload();
    });
}

function showAlertSuccess(){
    var c = 0;
        if (c == 0){
            document.getElementById('alert-success').style.display = 'block';
            c = 1;
            closeAlert();
        }
}

function showAlertError(){
    var c = 0;
        if (c == 0){
            document.getElementById('alert-error').style.display = 'block';
            c = 1;
            closeAlert();
        }
}


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
                        showAlertSuccess();
                        
                    },
                    eror: function(data){
                        showAlertError();
                    }
            });
        });
    });
});



