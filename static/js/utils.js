$(document).ready( function(){
  $("#convert").click(function(){
  if ($.trim($("#link").val()).length == 0) {
    $("#message").toggle(1000,'linear');
    $("#yt_form").toggle(1000,'linear');
    x=0;
    while (x<10) {
    $("#wait_message").delay(5000).toggle(3000,'linear');
    $("#wait_message").delay(5000).toggle(1000,'linear');
    x++;
    }
  }
 });//end click #convert
 $("#dl").click(function(){
    window.setTimeout(function() {
        window.location.href = '/';
    }, 180000);
 });//end click #dl
 if ($("#download").length) {
    window.setTimeout(function() {
        window.location.href = '/';
    }, 180000);
 };//end #download
});//end ready


