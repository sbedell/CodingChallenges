

// 	this.setDead = function() {
// 		this.isLive = false;
// 	};

// 	this.setLive = function() {
// 		this.isLive = true;
// 	};
// }

class Cell {
    constructor(id, x, y) {
        this.Id = Id || '';
        this.alive = false;
        this.coordinates = [x, y];
    }
    
    toggleState() {
        this.alive = !this.alive;
    }
}