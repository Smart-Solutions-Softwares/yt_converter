$(document).ready( function(){
  $("#convert").click(function(){
    $("#message").toggle(1000,'linear');
    $("#yt_form").toggle(1000,'linear');
    x=0;
    while (x<10) {
    $("#wait_message").delay(5000).toggle(3000,'linear');
    $("#wait_message").delay(5000).toggle(1000,'linear');
    x++;
    }
  });
});
window.setTimeout(function() {
    window.location.href = 'https://youtube-mp3-mp4.com';
}, 600000);

