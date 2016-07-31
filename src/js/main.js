$(document).ready(function(){
    // Sidebar toggling function
    var sidebar_visible = true;

    $("#toggle").click(function(){
        console.log("something");
        if (sidebar_visible === true) {
            sidebar_visible = false;
            $("#sidebar").animate({width: "0px", opacity: 0}, "fast");
        } else {
            sidebar_visible = true;
            $("#sidebar").animate({width: "200px", opacity:1}, "fast");
        }
    });
});
