class Cell {
    constructor(id, x, y) {
        this.Id = Id || '';
        this.alive = false;
        this.coordinates = [x, y];
    }
    
    toggleState() {
        this.alive = !this.alive;
    }
    
    setDead() {
        this.alive = false;
    }
    
    setAlive() {
        this.alive = true;
    }
}

class Board {
    constructor(xWidth, yHeight) {
        
    }
    
    getNeighbors(cell) {
        
    }
}

class StateChecker {
    constructor() {
        
    }
}