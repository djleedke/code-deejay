
var overlay = false;

function toggleNav(){
    if(overlay) {
        document.getElementById("overlay").style.width = "0%";
        overlay = false;
    } else {
        document.getElementById("overlay").style.width = "100%";
        overlay = true;
    }
}

/*
$(document).ready(function(){

    $.ajax({
        url: '/ajax/popular_posts/'
    })


});*/