$(document).ready(function(){
    toggle_sidebar();
    toggle_aside();
    $("article").sidenotes();
});

function toggle_sidebar() {
    var sidebar_visible = false;

    $("#sidebar-toggle").click(function(){
        if (sidebar_visible === true) {
            sidebar_visible = false;
            $("nav").removeClass("open");

        } else {
            sidebar_visible = true;
            $("nav").addClass("open");
        }
    });
}

function toggle_aside() {
    var aside_visible = false;

    $("#aside-toggle").click(function(){
        if (aside_visible === true) {
            aside_visible = false;
            $("aside").removeClass("open");

        } else {
            aside_visible = true;
            $("aside").addClass("open");
        }
    });
}

