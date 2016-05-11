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
            let colDiff = Math.abs(kingPos[0] - queenPos[0]);
            let rowDiff = Math.abs(kingPos[1] - queenPos[1]);
            if (colDiff == rowDiff) {
                return true;
            }
        }
        return false;
    }
}
