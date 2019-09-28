$(document).ready(function () {
    getDevices();
});

function getDevices() {
    let album_id = $('.edit_btn').attr('data-album');
    $.ajax({
        type: 'GET',
        cache: false,
        url: '/api/albums/',
        contentType: 'application/json',
        success: function (data) {
            for (let i=0; i < data.length; i++){
                if (data[i].album == album_id){
                    $('.post').html(data[i].post);
                    $('#comment_text').html(data[i].text);
                    $('.comment_author').html(data[i].author);
                }
            }
        }
    });
}
