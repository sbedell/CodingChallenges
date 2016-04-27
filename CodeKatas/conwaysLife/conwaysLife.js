class ConwayBoard {
    constructor(height, width) {
        this.height = height;
        this.width = width;
        this.cells = [];
    }
}

function generateCanvas() {
    document.getElementById("canvasSection").innerHTML = "";

    let newCanvas = document.createElement("canvas");
    newCanvas.height = document.getElementById("height").value;
    newCanvas.width = document.getElementById("width").value;
    newCanvas.id = "theCanvas";

    //Append it to the page:
    document.getElementById("canvasSection").appendChild(newCanvas);

    let context = document.getElementById("theCanvas").getContext("2d");

    context.strokeStyle = "#e1e1e1";
    context.fillStyle = "blue";
    context.fillRect(10, 10, newCanvas.height / 2, newCanvas.width / 2);
}
