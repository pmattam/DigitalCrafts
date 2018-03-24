// Conway's Game of Life!
// Game of Life is a deceptively simple description of a 2-dimensional simulation, 
// where each cell can either live or die depending on how many neighbors are alive or dead.

// Write a function, nextGeneration(), which takes in the current generation 
// (perhaps represented as a list of lists) and calculates the next generation based on the rules.

// Make sure your program works for some of the example patterns, 
// such as 2 "still life" patterns and 2 "oscillators".

var x = document.querySelector(".row-display");
// var day1 = [[false, false, false, false],
//             [false, true, true, false],
//             [false, true, true, false],
//             [false, false, false, false]];

// var day1 = [[false, false, false, false, false],
//             [false, false, true, false, false],
//             [false, true, false, true, false],
//             [false, false, true, false, false],
//             [false, false, false, false, false]];

// var day1 = [[false, false, false],
//             [true, true, true],
//             [false, false, false]];

var day1 = [[false, false, false, false, false, false],
            [false, false, false, false, false, false],
            [false, false, true, true, true, false],
            [false, true, true, true, false, false],
            [false, false, false, false, false, false],
            [false, false, false, false, false, false]];

var nextGeneration = function() {
    var day2 = [];
    for(var i=0; i<day1.length; i++) {
        var sublist = [];
        for(var j=0; j<day1[i].length; j++) {
            var neighbors = getNeighbors([i, j]);
            var lifeCheck = aliveOrDead([i, j], neighbors);
            sublist.push(lifeCheck);
        }
        day2.push(sublist);
    } 
    return day2;
}

var getNeighbors = function(cell) {
    var neighborsList = [];
    var i = cell[0];
    var j = cell[1];
    var previousRow = i-1;
    var nextRow = i+1;
    var previousCol = j-1;
    var nextCol = j+1;
    if(previousRow < 0) {
        previousRow = i;
    }
    if(previousCol < 0) {
        previousCol = j;
    }
    if(nextRow > day1.length-1) {
        nextRow = i;
    }
    if(nextCol > day1[0].length-1) {
        nextCol = j;
    }
    for(var k=previousRow; k<=nextRow; k++){
        for(var l=previousCol; l<=nextCol; l++) {
            if(k===i && l===j){
                continue; // i'm not the neighbor of myself
            }
            neighborsList.push([k, l]);
        }
    } 
    return neighborsList;
};

var aliveOrDead = function(cell, neighbors) {
    var i = cell[0];
    var j = cell[1];
    var count = countNeighborLives(neighbors);
    if(day1[i][j]){
        if(count < 2 || count > 3) {
            return false;
        }
        if(count === 2 || count === 3) {
            return true;
        }
    }  
    else {
        if(count === 3) {
            return true;
        }
    }
    return false;
};

var countNeighborLives = function(neighbors) {
    var count = 0;
    for (var k=0; k<neighbors.length; k++) {
        if(day1[neighbors[k][0]][neighbors[k][1]]) {
            count++;    
        }
    }
    return count;
}

var displayGrid = function(day) {
    var removeList = [];
    day.forEach(function(row) {
        var p = document.createElement('p');
        var displayStr = "";
        row.forEach(function(cell) {
            if(cell) {
                displayStr += " O";
            }
            else {
                displayStr += " X";
            }
        });
        p.textContent = displayStr;
        x.appendChild(p);
        removeList.push(p);
    });
    setTimeout(function() 
    {
        removeList.forEach(function(value) {
        x.removeChild(value);
        });
    }, 1000);
};

var gameOfLife = function () {
    displayGrid(day1);
    day1 = nextGeneration(day1);
}

setInterval(gameOfLife, 2000);
