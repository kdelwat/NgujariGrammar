$(document).ready(function(){
    toggle_sidebar();

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

function toggle_sidebar() {
    var sidebar_visible = false;

    if ($(window).width() > 800) {
        sidebar_visible = true;
        $("nav").addClass("open");
    }

    $("#sidebar-toggle").click(function(){
        if (sidebar_visible === true) {
            sidebar_visible = false;
            $("nav").removeClass("open");

        } else {
            sidebar_visible = true;
            $("nav").addClass("open");
        }
    });

    $(window).resize(function() {
        if ($(this).width() <= 1000 && sidebar_visible === true) {
            sidebar_visible = false;
            $("nav").removeClass("open");
        } else if ($(this).width() > 1000 && sidebar_visible === false) {
            sidebar_visible = true;
            $("nav").addClass("open");
        }
    });
}


