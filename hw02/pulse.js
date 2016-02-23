var c = document.getElementById("canvas");
var pul = document.getElementById("button1");
var ctx = c.getContext("2d");
var diff = -1;
var rad = 0;

ctx.fillStyle = "#ff0000";
var col = 1;

var pulse = function pulse(e) {
    ctx.clearRect(0, 0, c.width, c.height);
    if(rad == c.width/2 || rad == 0){
	diff = diff * -1;
	if(col == 1){
	    ctx.fillStyle = "#00ff00";
	    col = 2;
	}else if(col == 2){
	    ctx.fillStyle = "#0000ff";
	    col = 3;
	}else{
	    ctx.fillStyle = "#ff0000";
	    col = 1;
	}
    }
    rad = rad + diff;
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, rad, 0, 2*Math.PI);
    ctx.fill();
    window.requestAnimationFrame(pulse);
}



pul.addEventListener("click",pulse);
