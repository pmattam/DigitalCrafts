const assert = require('assert');

let getLatticePointRows = gridSize => {
    return gridSize + 1;
}
assert.deepStrictEqual(getLatticePointRows(2), 3, "Lattice Point Rows are not expected");

let getLatticePointColumns = gridSize => {
    return gridSize + 1;
}
assert.deepStrictEqual(getLatticePointColumns(2), 3, "Lattice Point Columns are not expected");

let findLatticePointsValues = (rows, columns) => {
    let grid = [];
    for (i = 0; i < rows; i++) {
        var addRow = [];
        for (j = 0; j < columns; j++) {
            if (i === 0) {
                addRow.push(1);
            } else {
                if (j === 0) {
                    addRow.push(1);
                } else {
                    addRow.push(addRow[j - 1] + grid[i - 1][j]);
                }
            }
        }
        grid.push(addRow);
    }
    console.log(grid[rows - 1][columns - 1]);
    return grid[rows - 1][rows - 1];
};

assert.deepStrictEqual(findLatticePointsValues(getLatticePointRows(2), getLatticePointColumns(2)), 6, "Test Failed for 2x2");
assert.deepStrictEqual(findLatticePointsValues(getLatticePointRows(3), getLatticePointColumns(3)), 20, "Test Failed for 3x3");
assert.deepStrictEqual(findLatticePointsValues(getLatticePointRows(4), getLatticePointColumns(4)), 70, "Test Failed for 4x4");
assert.deepStrictEqual(findLatticePointsValues(getLatticePointRows(5), getLatticePointColumns(5)), 252, "Test Failed for 5x5");
assert.deepStrictEqual(findLatticePointsValues(getLatticePointRows(20), getLatticePointColumns(20)), 137846528820, "Test Failed for 20x20")