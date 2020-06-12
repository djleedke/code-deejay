
var overlay = false;

function toggleNav(){
    if(overlay) {
        document.getElementById("overlay").style.height = "0";
        document.getElementById("overlay").style.maxheight = "0%";
        overlay = false;
    } else {
        document.getElementById("overlay").style.height = "auto";
        document.getElementById("overlay").style.maxHeight = "1000px";
        overlay = true;
    }
}