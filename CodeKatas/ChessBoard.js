/*
    TODO:
    1. fix the class - add more methods and properties
    2. make a clear board function which clears pieces off the board
*/
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

let rows;
let cols;
let board;
let queenPos;
let kingPos;
function generateBoard() {
    clearBoard();
    rows = document.getElementById("rows").value;
    cols = document.getElementById("columns").value;
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

function clearBoard() {
    document.getElementById("chessboard").innerHTML = "";
    document.getElementById("outputText").innerHTML = "";
}

// Draws the king and queen on the board
function drawKingAndQueen() {
    let king = document.getElementById("kingCoords").value.split(",");
    let queen = document.getElementById("queenCoords").value.split(",");

    let kingCol = parseInt(king[0].trim()) - 1;
    let kingRow = parseInt(king[1].trim()) - 1;
    // Validation Check
    if (kingCol >= cols || kingRow >= rows) {
        alert("King is off the board!");
        return;
    }

    let queenCol = parseInt(queen[0].trim()) - 1;
    let queenRow = parseInt(queen[1].trim()) - 1;
    // Validation check
    if (queenCol >= cols || queenRow >= rows) {
        alert("Queen is off the board!");
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

    // set global variables
    queenPos = [queenCol, queenRow];
    kingPos = [kingCol, kingRow];
}
// and checks if the king is in check from the queen
function kingInCheck() {
    drawKingAndQueen();

    // using global variables
    if (board.isKingThreatened(kingPos, queenPos)) {
        document.getElementById("outputText").innerHTML = "King is in check!";
    } else {
        document.getElementById("outputText").innerHTML = "King is NOT in check.";
    }
}

// let myBoard = new ChessBoard(10, 10);
// console.log(myBoard.isKingThreatened([1, 2], [2, 3]));
// console.log(myBoard.isKingThreatened([1, 3], [8, 3]));
// console.log(myBoard.isKingThreatened([1, 1], [5, 5]));
// console.log(myBoard.isKingThreatened([1, 1], [1, 4]));
// console.log(myBoard.isKingThreatened([1, 1], [4, 1]));
// console.log(myBoard.isKingThreatened([1, 1], [7, 3]));
