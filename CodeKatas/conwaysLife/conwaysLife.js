class ConwayBoard {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.context = canvasElement.getContext("2d");
        this.context.fillStyle = "blue";
        this.context.strokeStyle = "#e3e3e3";
        
        // 2d array filled with true or false values,
        // true means the cell is/should be filled in:
        this.cells = [];
    }
    
    drawGrid() {
        for (let x = 0; x < this.canvas.height; x++) {
            for (let y = 0; y < this.canvas.width; y++) {
                this.context.beginPath();
                this.context.rect(x * 10, y * 10, 10, 10);
                this.context.stroke();
            }
        }
    }
    
    clearCanvas() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
    
    drawSquare(xCoord, yCoord) {
        this.context.fillRect(xCoord, yCoord, this.canvas.width / 2, this.canvas.height / 2);
    }
    
    animateSquare() {
    }
}

// Global Variable:
let _theGameBoard;

function initCanvas() {
    // clear the canvas section first:
    document.getElementById("canvasSection").innerHTML = "";

    let newCanvas = document.createElement("canvas");
    newCanvas.height = document.getElementById("height").value * 5;
    newCanvas.width = document.getElementById("width").value * 5;
    newCanvas.id = "theCanvas";

    //Append it to the page:
    document.getElementById("canvasSection").appendChild(newCanvas);
    
    // use the constructor:
    _theGameBoard = new ConwayBoard(newCanvas);
    _theGameBoard.drawGrid();
    _theGameBoard.drawSquare(10, 10);
}

function clearCanvas() {
    _theGameBoard.clearCanvas();
}