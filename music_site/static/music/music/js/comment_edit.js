$('#modalComments').on('show.bs.modal', function(){
    $(this).find('input[name = "post"]')[0].value = $('.edit_btn').attr('data-post');
    $(this).find('input[name = "text"]')[0].value = $('.edit_btn').attr('data-text');
});


$(document).delegate('#form-edit-btn', 'click', function(event){
    let modal = $('#modalComments');
    let post_id = $('.edit_btn').attr('data-id');
    let csrf = $('[name="csrfmiddlewaretoken"]').attr('value');
    let each_data = {
        post: modal.find('#edit input[name="post"]')[0].value,
        text: modal.find('#edit input[name="text"]')[0].value,
        author: $('.edit_btn').attr('data-author'),
        album: $('.edit_btn').attr('data-album'),
    }
    $.ajax({
        type: 'PUT',
        url: '/api/albums/' + post_id + '/edit/',
        headers: {"X-CSRFToken": csrf},
        data: {
            'post': each_data['post'],
            'text': each_data['text'],
        },
        success: function(data){
            document.getElementById("comment_post").innerHTML=data.post;
            document.getElementById("comment_text").innerHTML=data.text;
            modal.modal('hide');
            $('.modal-backdrop').hide();
        }
    });
});

