var canvas = document.getElementById("displayCanvas");
var ctx = canvas.getContext("2d");
const pixelGrid = [];
const rect = canvas.getBoundingClientRect();
var xScale = rect.width/16;
var yScale = rect.height/16;
var boolDrawBorder = true;

class Tile
{
    constructor(x , y, colorOfTile){
        this.colorOfTile = colorOfTile;
        this.x = x;
        this.y = y;
    }
}

function Initialize()
{
    var _x, _y;
    for (_y=0; _y< 16; _y++)
    {
        for (_x=0; _x< 16; _x++)
        {
            pixelGrid.push(new Tile(_x, _y, "#00FF00"));
        }
    }
    DrawCanvas();
}

function DrawCanvas()
{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var _x, _y;
    for (_y=0; _y< 16; _y++)
    {
        for (_x=0; _x< 16; _x++)
        {
            var pos = (_y*16)+_x;
            DrawTile(pixelGrid[pos]);
        }
    }
}

function DrawTile(_tile)
{
    var _locX = Math.floor(_tile.x*xScale);
    var _locY = Math.floor(_tile.y*yScale);
    ctx.fillStyle = _tile.colorOfTile;
    ctx.fillRect(_locX, _locY, xScale, yScale);
    if (boolDrawBorder == true){
        DrawBorder(_locX, _locY);
    }
}

function DrawBorder(x,y)
{
    ctx.strokeRect(x,y,xScale, yScale);
}

function ChangeTileColor(x,y, colorToChange)
{
    var index = (y*16)+x; 
    pixelGrid[index].colorOfTile = colorToChange;
    DrawCanvas();
}

function getCursorPosition(canvas, event) {
    const x = Math.floor((event.clientX - rect.left)/xScale);
    const y = Math.floor((event.clientY - rect.top)/yScale);
    console.log("x: " + x + " y: " + y);
    ChangeTileColor(x,y, "#800000");
}

canvas.addEventListener('mousedown', function(e) {
    getCursorPosition(canvas, e)
})