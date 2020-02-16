var audio;
var default_volume = 0.5
var album_image = $("#audio-img img").attr("src");

// function change image
function changeImage(){

};

// Setup background image
document.getElementById("container-flud").style.backgroundImage = 'url(' + album_image + ')';

//Pause button
$('#pause').hide();


//Init
initAudio($('#playlist li:first-child'));

//Init function
function initAudio(element){
    var full_path = element.attr('path');
    var title = element.text();
    var artist = element.attr('artist');
    var song = element.attr('song');
    var image_album = element.attr('album-image');

    // Create Audio
    audio = new Audio(full_path + song);
    
    audio.volume = default_volume;

    $('#audio-img img').attr('src', image_album);

    if (!audio.currentTime){
        $('#duration').html('0:00');
    }

    $('#audio-player .title').text(title);
    $('#audio-player .artist').text(artist);

    $('#playlist li').removeClass('active');
    element.addClass('active');

}

//Play button
$('#play').click(function(){
    audio.play();
    $('#play').hide();
    $('#pause').show();
    $('#duration').fadeIn(400);
    showDuration();
});

//Pause button
$('#pause').click(function(){
    audio.pause();
    $('#pause').hide();
    $('#play').show();
    $('#duration').fadeIn(400);
});

//Stop button
$('#stop').click(function(){
    audio.pause();
    audio.currentTime = 0;
    $('#pause').hide();
    $('#play').show();
    $('#duration').fadeOut(400);
});


//Time duration
function showDuration(){
    $(audio).bind('timeupdate',function(){
        var second = parseInt(audio.currentTime % 60);
        var minute = parseInt((audio.currentTime) / 60) % 60;
        if (second < 10){
            second = '0' + second
        }
        if (second == Math.round(audio.duration) && $('#playlist li:last-child')){
            if ($('#pause').is(':visible')){
                $('#play').show();
                $('#pause').hide();
            }
        }
        else{
            if( audio.currentTime >= audio.duration){
                $('#next').trigger('click');
            }
        }
        $('#duration').html(minute + ':' + second);
        var value = 0;
        if (audio.currentTime > 0){
            value = Math.floor((100 / audio.duration) * audio.currentTime)
        }
        $('#progress').css('width',value+'%');
    })
}


//Next button
$('#next').click(function(){
    audio.pause();
    var next = $('#playlist li.active').next();
    if (next.length == 0){
        next = $('#playlist li:first-child');
    }
    if($('#play').is(':visible')){
        $('#play').hide();
        $('#pause').show();
    }
    initAudio(next);
    audio.play();
    $("")
    showDuration();

});

//Prev button
$('#prev').click(function(){
    audio.pause();
    var prev = $('#playlist li.active').prev();
    if (prev.length == 0){
        prev = $('#playlist li:last-child');
    }
    if($('#play').is(':visible')){
        $('#play').hide();
        $('#pause').show();
    }
    initAudio(prev);
    audio.play();
    showDuration();
});

//Volume settings
$('#volume').change(function(){
    default_volume = parseFloat(this.value / 10);
    audio.volume = default_volume;
})

//Play always
$(audio).on('ended',function(){
    var next = $('#playlist li.active').next();
    if (next.length == 0){
        next = $('#playlist li:first-child');
    }
    initAudio(next);
    audio.play();
    showDuration();
});

//Rewind
$("#progressbar").mouseup(function(e){
    var leftOffset = e.pageX - $(this).offset().left;
    var songPercents = leftOffset / $('#progressbar').width();
    audio.currentTime = parseFloat(songPercents * audio.duration);
});

//Click for playing
$('#playlist li').click(function(){
    audio.pause();
    initAudio($(this));
    audio.play();
    showDuration
    $('#play').hide();
    $('#pause').show();
});
