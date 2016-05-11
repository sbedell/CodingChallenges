let myBoard = new ChessBoard(5, 5);

QUnit.module("Chessboard Tests", () => {
    QUnit.test("Test row count", assert => {
        assert.equal(5, myBoard.rows);
    });

    QUnit.test("Test column count", assert => {
        assert.equal(5, myBoard.columns);
    });

    QUnit.test("Test King in Check", assert => {
        assert.equal(true, myBoard.isKingThreatened([1, 1], [1, 5]));
        assert.equal(true, myBoard.isKingThreatened([1, 3], [4, 3]));
        assert.equal(true, myBoard.isKingThreatened([1, 1], [3, 3]));
    });

    QUnit.test("Test King not in check", assert => {
        assert.equal(false, myBoard.isKingThreatened([1, 1], [2, 3]));
    });
});
