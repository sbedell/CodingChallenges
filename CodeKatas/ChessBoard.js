class ChessBoard {
    constructor(rows, columns) {
        this.rows = rows;
        this.columns = columns;
    }

    // KingPos and QueenPos are both arrays of length 2,
    // first position is the column, second pos is the row
    isKingThreatened(kingPos, queenPos) {
        if (kingPos[0] == queenPos[0]) { // checking column
            return true;
        } else if (kingPos[1] == queenPos[1]) {  // checking row
            return true;
        } else {  // check diagonals next
            let colDiff = kingPos[0] - queenPos[0];
            let rowDiff = kingPos[1] - queenPos[1];
            if (colDiff == rowDiff) {
                return true;
            }
        }
        return false;
    }
}

var rows;
var cols;
function generateBoard() {
    clearBoard();
    rows = document.getElementById("rows").value;
    cols = document.getElementById("columns").value;
    if (rows <= 0 || cols <= 0) {
        alert("Cannot have 0 or less columns or rows. Exiting");
        return;
    }
    var board = new ChessBoard(rows, cols);

    var boardElement = document.getElementById("chessboard");
    for (let i = 0; i < rows; i++) {
        let row = boardElement.insertRow();
        row.id = "row" + i;
        for (let x = 0; x < cols; x++) {
            let newCell = row.insertCell();
            //newCell.innerHTML = "fucksalt";
            // id is like col1row3
            newCell.id = `col${x}row${i}`;
        }
    }
}

function clearBoard() {
    document.getElementById("chessboard").innerHTML = "";
    document.getElementById("outputText").innerHTML = "";
}

function kingInCheck() {
    let king = document.getElementById("kingCoords").value.split(",");
    let queen = document.getElementById("queenCoords").value.split(",");
    let kingCol = parseInt(king[0].trim()) - 1;
    let kingRow = parseInt(king[1].trim()) - 1;
    if (kingCol >= cols) {
        alert("off the board!")
        return;
    }
    let kingId = `col${kingCol}row${kingRow}`;
    let queenCol = parseInt(queen[0].trim()) - 1;
    let queenRow = parseInt(queen[1].trim()) - 1;
    let queenId = `col${queenCol}row${queenRow}`;
    document.getElementById(kingId).innerHTML = "K";
    document.getElementById(queenId).innerHTML = "Q";
    // document.getElementById("outputText").innerHTML = "King is maybe in check";
}

// let myBoard = new ChessBoard(10, 10);
// console.log(myBoard.isKingThreatened([1, 2], [2, 3]));
// console.log(myBoard.isKingThreatened([1, 3], [8, 3]));
// console.log(myBoard.isKingThreatened([1, 1], [5, 5]));
// console.log(myBoard.isKingThreatened([1, 1], [1, 4]));
// console.log(myBoard.isKingThreatened([1, 1], [4, 1]));
// console.log(myBoard.isKingThreatened([1, 1], [7, 3]));
