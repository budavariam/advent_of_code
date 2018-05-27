export function solution(input: string[], options?: any) {
    const favouriteNumber = parseInt(input[0], 10);
    const map = new Labyrinth(favouriteNumber);
    const pathFinder = new PathFinder(map);

    const [startX, startY] = Labyrinth.splitCoord(options.start);
    const start = new Path(startX, startY, 0);
    const destination = options.destination;
    return "" + pathFinder.shortestPath(start, destination);
}

enum Field {
    EMPTY = ".",
    FILLED = "#",
    VISITED = "x",
}

class Path {
    public static readonly directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ];

    constructor(
        public x: number,
        public y: number,
        public distance: number,
    ) {}

    public toString() {
        return `${this.x},${this.y}`;
    }
}

class Labyrinth {
    public static splitCoord(rawCoord: string): number[] {
        return rawCoord.split(",").map((coord) => parseInt(coord, 10));
    }

    private map = new Map <string, Field> ();
    private mapSeed: (x: number, y: number) => Field;
    private maxWidth = 0;
    private maxHeight = 0;

    constructor(favouriteNumber: number) {
        this.mapSeed = this.initMapSeedCounter(favouriteNumber);
    }

    public fieldState(coord: string): Field {
        return this.map.get(coord) || Field.EMPTY;
    }

    public canMove(x: number, y: number) {
        const coord = `${x},${y}`;
        this.maxWidth = Math.max(x, this.maxWidth);
        this.maxHeight = Math.max(y, this.maxHeight);
        const state = this.map.get(coord);
        if (state && state === Field.EMPTY) {
            this.map.set(coord, Field.VISITED);
            return true;
        } else if (!state) {
            const newField = this.mapSeed(x, y);
            this.map.set(coord, newField);
            return newField === Field.EMPTY;
        } else {
            return false;
        }
    }

    public moveFourDirections(current: Path): Path[] {
        const result: Path[] = [];
        for (const [xmove, ymove] of Path.directions) {
            const newX = current.x + xmove;
            const newY = current.y + ymove;
            if (newX >= 0 && newY >= 0 && this.canMove(newX, newY)) {
                result.push(new Path(newX, newY, current.distance + 1));
            }
        }
        return result;
    }

    private initMapSeedCounter(addendum: number) {
        function countOneBits(num: number) {
            const binaryrepr = num.toString(2);
            let result = 0;
            for (const binary of binaryrepr) {
                if (binary === "1") {
                    result++;
                }
            }
            return result;
        }

        return (x: number, y: number): Field =>
            countOneBits(x * x + 3 * x + 2 * x * y + y + y * y + addendum) % 2 === 0 ? Field.EMPTY : Field.FILLED;
    }
}

class PathFinder {
    private queue: Path[] = [];

    constructor(private map: Labyrinth) {}

    public shortestPath(start: Path, destination: string): number {
        this.queue.push(start);
        while (this.queue.length > 0) {
            const currentPath: Path = this.queue.shift() as Path;
            this.queue = this.queue.concat(this.map.moveFourDirections(currentPath));
            if (currentPath.toString() === destination) {
                return currentPath.distance;
            }
        }

        return -1;
    }
}
