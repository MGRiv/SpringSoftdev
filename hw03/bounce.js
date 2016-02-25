var c = document.getElementById("canvas");
var ctx = c.getContext("2d");
var b = document.getElementById("button1");
var s = document.getElementById("button2");
var frameid;
var img = new Image();
img.src = "ball.png";



var bounce = function bounce(e) {
    window.cancelAnimationFrame(frameid);
    var posx = Math.floor(Math.random() * 300) + 100;
    var posy = Math.floor(Math.random() * 300) + 100;
    var xdiff = 1;    
    var ydiff = 0;
    var mod = .05;
    var move = function (e) {
	ctx.clearRect(0,0,500,500);
	posx += xdiff;
	posy += ydiff;
	if(posx < 0 || posx > 460){
	    posx -= xdiff;
	    xdiff *= -1;
	}
	if(posy > 460){
	    posy -= ydiff;
	    ydiff *= -1;
	}
	ydiff += mod;
	ctx.drawImage(img,posx,posy,40,40);
	frameid = window.requestAnimationFrame(move);
    };
    move();
};

var cease = function cease(e) {
    window.cancelAnimationFrame(frameid);
}

b.addEventListener("click",bounce);
s.addEventListener("click",cease);
