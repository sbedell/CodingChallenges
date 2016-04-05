class ChessBoard {
    constructor(rows, columns) {
        this.rows = rows;
        this.columns = columns;
        this.queenPos = [];
        this.kingPos = [];
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

let board;
function generateBoard() {
    clearBoard();
    let rows = document.getElementById("rows").value;
    let cols = document.getElementById("columns").value;
    if (rows <= 0 || cols <= 0) {
        alert("Cannot have 0 or less columns or rows!");
        clearBoard();
        return;
    }
    board = new ChessBoard(rows, cols);

    let boardElement = document.getElementById("chessboard");
    for (let x = 0; x < rows; x++) {
        let row = boardElement.insertRow();
        // row.id = "row" + i;
        for (let y = 0; y < cols; y++) {
            let newCell = row.insertCell();
            newCell.id = `col${y}row${x}`;
            // if odd cell, color it black
            if ((x + y + 1) % 2 == 0) {
                newCell.className = 'blackSquare';
            }
        }
    }
}

function resetBoard() {
    if (window.confirm("Are you sure you want to reset the board?")) {
        clearBoard();
    }
}

function clearBoard() {
    document.getElementById("chessboard").innerHTML = "";
    document.getElementById("outputText").innerHTML = "";
}

function clearPieces() {
    let tds = document.getElementsByTagName("td");
    //console.dir(tds);
    for (let x = 0; x < tds.length; x++) {
        tds[x].innerText = '';
    }
    document.getElementById("outputText").innerHTML = "";
}

// and checks if the king is in check from the queen
function kingInCheck() {
    clearPieces();

    let kingCoords = document.getElementById("kingCoords").value;
    let queenCoords = document.getElementById("queenCoords").value;
    if (kingCoords.indexOf(",") == -1 || queenCoords.indexOf(",") == -1) {
        alert("Coordinates need to be comma separated values");
        return;
    }

    let kingCol = parseInt(kingCoords.split(",")[0].trim()) - 1;
    let kingRow = parseInt(kingCoords.split(",")[1].trim()) - 1;
    if (kingCol >= board.columns || kingRow >= board.rows) {
        alert("King is off the board!");
        return;
    }

    let queenCol = parseInt(queenCoords.split(",")[0].trim()) - 1;
    let queenRow = parseInt(queenCoords.split(",")[1].trim()) - 1;
    if (queenCol >= board.columns || queenRow >= board.rows) {
        alert("Queen is off the board!");
        return;
    }

    if ((queenCol == kingCol) && (queenRow == kingRow)) {
        alert("Queen and King cannot be on the same square");
        return;
    }

    let queenSquare = document.getElementById(`col${queenCol}row${queenRow}`);
    let kingSquare = document.getElementById(`col${kingCol}row${kingRow}`);
    kingSquare.innerHTML = "K";
    queenSquare.innerHTML = "Q";
    if (kingSquare.className == 'blackSquare') {
        kingSquare.style.color = 'white';
    }
    if (queenSquare.className == 'blackSquare') {
        queenSquare.style.color = 'white';
    }

    // set class variables
    board.queenPos = [queenCol, queenRow];
    board.kingPos = [kingCol, kingRow];

    // using global variables
    if (board.isKingThreatened(board.kingPos, board.queenPos)) {
        document.getElementById("outputText").innerHTML = "<strong>King is in check!</strong>";
    } else {
        document.getElementById("outputText").innerHTML = "King is <strong>NOT</strong> in check.";
    }
}

// Generic Usage examples/tests:

// let myBoard = new ChessBoard(10, 10);
// console.log(myBoard.isKingThreatened([1, 2], [2, 3]));
// console.log(myBoard.isKingThreatened([1, 3], [8, 3]));
// console.log(myBoard.isKingThreatened([1, 1], [5, 5]));
// console.log(myBoard.isKingThreatened([1, 1], [1, 4]));
// console.log(myBoard.isKingThreatened([1, 1], [4, 1]));
// console.log(myBoard.isKingThreatened([1, 1], [7, 3]));
