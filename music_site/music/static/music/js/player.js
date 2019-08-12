var audio;

//Pause button
$('#pause').hide();

//Init
initAudio($('#playlist li:first-child'));

//Init function
function initAudio(element){
    var full_path = element.attr('path');
    var title = element.text();
    var artist = element.attr('artist');
    var song = element.attr('song')

    // Create Audio
    audio = new Audio(full_path + song);

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
        $('#duration').html(minute + ':' + second);
        var value = 0;
        if (audio.currentTime > 0){
            value = Math.floor((100 / audio.duration ) * audio.currentTime);
        }
        $('#progress').css('width',value+'%');
    })
}

//Next button
$('#next').click(function(){
    audio.pause();
    var next = $('#playlist li.active').next();
    if (next.length == 0){
        next = $('#playlist li.first-child');
    }
    initAudio(next);
    audio.play();
    showDuration();
});

//Prev button
$('#prev').click(function(){
    audio.pause();
    var prev = $('#playlist li.active').prev();
    if (prev.length == 0){
        prev = $('#playlist li.last-child');
    }
    initAudio(prev);
    audio.play();
    showDuration();
});

//Volume settings
$('#volume').change(function(){
    audio.volume = parseFloat(this.value / 10);
})

//Play always
$(audio).on('ended',function(){
    audio.pause();
    var next = $('#playlist li.active').next();
    if (next.length == 0){
        next = $('#playlist li.first-child');
    }
    initAudio(next);
    audio.play();
    showDuration();
});

