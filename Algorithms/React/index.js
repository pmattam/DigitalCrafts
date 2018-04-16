const root = document.querySelector('.react-root');

var nextGeneration = function(day1) {
    var day2 = [];
    for(var i=0; i<day1.length; i++) {
        var sublist = [];
        for(var j=0; j<day1[i].length; j++) {
            var neighbors = getNeighbors(day1, [i, j]);
            var lifeCheck = aliveOrDead(day1, [i, j], neighbors);
            sublist.push(lifeCheck);
        }
        day2.push(sublist);
    } 
    return day2;
}

var getNeighbors = function(day1, cell) {
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

var aliveOrDead = function(day1, cell, neighbors) {
    var i = cell[0];
    var j = cell[1];
    var count = countNeighborLives(day1, neighbors);
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

var countNeighborLives = function(day1, neighbors) {
    var count = 0;
    for (var k=0; k<neighbors.length; k++) {
        if(day1[neighbors[k][0]][neighbors[k][1]]) {
            count++;    
        }
    }
    return count;
}

let Title = () => <h1 className="title-div">REACTIFIED GAME OF LIFE!</h1>

let startPlay = (grid, setNewGrid, setIntervalId) => {
    let id = setInterval(() => {
        let newGrid = nextGeneration(grid);
        setNewGrid(newGrid);
        grid = newGrid;
    }, 1000);
    setIntervalId(id);
};

let getRegeneratedRandomCellVal = () => {
    let val = Math.floor(Math.random() * 4);
    console.log(val);
    if (val === 1) {
        return true;
    } else {
        return false;
    }
};

let regenerateRandomSeeds = (setNewGrid) => {
    let rows = 10;
    let columns = 10;
    let newRandomGrid = Array(rows).fill().map(() => Array(columns).fill().map(getRegeneratedRandomCellVal));
    setNewGrid(newRandomGrid);
};

let clearGameBoard = (intervalId, setNewGrid) => {
    let rows = 10;
    let columns = 10;
    let clearGrid = Array(rows).fill().map(() => Array(columns).fill(false));
    clearInterval(intervalId);
    setNewGrid(clearGrid);
};

let PlayButton = ({ grid, setNewGrid, setIntervalId}) => 
    <div className="play-div">
        <button className="playButton" onClick={() => startPlay(grid, setNewGrid, setIntervalId)}>PLAY</button>
    </div>

let PauseButton = ({ intervalId }) =>
    <div className="pause-div">
        <button className="pauseButton" onClick={() => clearInterval(intervalId)}>PAUSE</button>
    </div>

let NewRandomSeedsButton = ({ setNewGrid }) =>
    <div className="random-div">
        <button className="randomButton" onClick={() => regenerateRandomSeeds(setNewGrid)}>RANDOM</button>
    </div>  

let ClearGameButton = ({ intervalId, setNewGrid }) =>
    <div className="clear-div">
        <button className="clearButton" onClick={() => clearGameBoard(intervalId, setNewGrid)}>CLEAR</button>
    </div>

let Grid = ({ grid }) => {
    let rows = grid.length;
    let cols = grid[0].length;
    return (
        <div className="grid">
            {
                grid.map(row => 
                <EachRow 
                    row={row}
                />)
            }
        </div>
    )
};

let getColClassName = (col) => {
    if(col) {
        return "box-alive";
    }
    else {
        return "box-dead";
    }
};

let EachRow = ({ row }) => 
    <div className="each-row">
        {   
            row.map(col => 
            <div className={getColClassName(col)}>
            </div>)
        }
    </div>

class Main extends React.Component {

    constructor(props) {
        super(props);
        this.rows = 10;
        this.columns = 10;

        let getRandomCellVal = () => {
            let val = Math.floor(Math.random() * 4);
            console.log(val);
            if (val === 1) {
                return true;
            } else {
                return false;
            }
        };

        this.state = {
            grid: Array(this.rows).fill().map(() => Array(this.columns).fill().map(getRandomCellVal)),
            intervalId: null
        }
    }

    render() {
        let { grid, intervalId } = this.state;

        let setNewGrid = (newGrid) => {
            this.setState({
                grid: newGrid
            })
        }

        let setIntervalId = (newIntervalId) => {
            this.setState({
                intervalId: newIntervalId
            })
        } 

        return (
            <div className="grid-div">
                <Title />
                <div className="buttons-div"> 
                    <PlayButton
                        grid={grid}
                        setNewGrid={setNewGrid}
                        setIntervalId={setIntervalId}
                    />
                    <PauseButton 
                        intervalId={intervalId}
                    />
                    <NewRandomSeedsButton 
                        setNewGrid={setNewGrid}
                    />
                    <ClearGameButton
                        intervalId={intervalId}
                        setNewGrid={setNewGrid}
                    />
                </div>
                
                <Grid
                    grid={grid}
                />
            </div>
        )      
    }
}

ReactDOM.render( <Main /> , root);