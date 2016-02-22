var c = document.getElementById("canvas");
var cl = document.getElementById("button");
var ctx = c.getContext("2d");

ctx.fillStyle = "#dd0000";
ctx.beginPath();
var clear = function clear(e) {
    e.preventDefault();
    ctx.clearRect(0,0,500,500);
    ctx.beginPath();
};

var dot = function dot(e) {
    e.preventDefault();
    ctx.lineTo(e.offsetX,e.offsetY);
    ctx.closePath();
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(e.offsetX,e.offsetY,10,0,2*Math.PI);
    ctx.fill();
    ctx.moveTo(e.offsetX,e.offsetY);
};

cl.addEventListener("click",clear);
c.addEventListener("click",dot);
