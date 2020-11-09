function DrawOnCanvas()
{
    var canvas = document.getElementById("displayCanvas");
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#000000";
    ctx.fillRect(0,0,1,1);
    ctx.fillStyle = "#800000";
    ctx.fillRect(1,1,10,10);
}