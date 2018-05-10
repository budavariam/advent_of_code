export function solution(input: string[]) {
    const parsed = parseInput(input[0]);
    const coords = processData(parsed);
    const distance = calcDistance(coords);
    return "" + Math.abs(distance);
}

function parseInput(input: string): Direction[] {
    return input
        .split(", ")
        .map((elem: string) => new Direction(elem.charAt(0) === "R" ? "R" : "L", parseInt(elem.slice(1), 10)));
}

function processData(parsed: Direction[]): CoordNumbers {
    const position = new Position();
    parsed.forEach((element) => position.move(element));
    return position.currentPosition();
}

function calcDistance(coords: CoordNumbers): number {
    return coords[0] + coords[1];
}

type Quarter = "N" | "E" | "W" | "S";
type Dirs = "R" | "L";
type Coords = "x" | "y";
type CoordNumbers = [number, number];
type DirectionMap = { [k in Quarter]: { [l in Dirs]: Quarter } };
type StepMap = { [k in Quarter]: [Coords, number] };

class Direction {
    constructor(
        public direction: Dirs,
        public count: number) {}
}

class Position {
    private x = 0;
    private y = 0;
    private direction: Quarter = "N";
    private directions: DirectionMap = {
        E: {R: "S", L: "N"},
        N: {R: "E", L: "W"},
        S: {R: "W", L: "E"},
        W: {R: "N", L: "S"},
    };
    private step: StepMap = {
        E: ["x",  1],
        N: ["y",  1],
        S: ["y", -1],
        W: ["x", -1],
    };
    constructor() {}

    public currentPosition(): CoordNumbers {
        return [this.x, this.y];
    }

    public move(newDir: Direction) {
        this.turn(newDir.direction);
        this.adjustPosition(newDir.count);
    }

    private turn(direction: Dirs) {
        this.direction = this.directions[this.direction][direction];
    }

    private adjustPosition(count: number) {
        const moveBy = this.step[this.direction];
        if (moveBy[0] === "x") {
            this.x += count * moveBy[1];
        } else {
            this.y += count * moveBy[1];
        }
    }
}
