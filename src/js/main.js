$(document).ready(function(){
    $("div.content").sidenotes();

    if ($(window).width() <= 979) {
        $("div.content").sidenotes("hide");
    }

    $(window).resize(function() {
        if ($(this).width() <= 979) {
            $("div.content").sidenotes("hide");
        } else {
            $("div.content").sidenotes("show");
        }
    });

});
