var c = document.getElementById("canvas");
var ctx = c.getContext("2d");
var b = document.getElementById("button1");
var s = document.getElementById("button2");
var xdiff = 1;
var posx = c.width/2;
var posy = c.height/2;
    
var ydiff = 1;
var frameid;
var img;

b.addEventListener("click",bounce);
window.onload = function() {
    img = new Image();
    img.src = "ball.png"
    ctx.drawImage(img,c.width/2,c.height/2,25,25);
}

var bounce = function bounce(e) {
    ctx.clearRect(0,0,c.width,c.height);
    if(
    ctx.drawImage(img,posx,posy,25,25);
    if
}
