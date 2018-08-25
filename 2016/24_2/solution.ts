export function solution(input: string[], options?: any) {
    const maze = new Maze(input);
    const distanceMatrix = maze.calculateDistances();
    return "" + maze.getShortestDistances(distanceMatrix);
}

interface IPosition {
    x: number;
    y: number;
    elem: string;
}

type Locations = {[x in string]: boolean};
type DistanceMatrix = {[x in string]: {[y in string]: number}};

class Maze {
    public readonly directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ];

    private POI: IPosition[] = [];
    private poiLocations: {[x in string]: IPosition} = {};
    private WALL: Locations = {};

    constructor(input: string[]) {
        input.forEach((line, rowNum) => {
            line.split("").map((elem, colNum) => {
                if (elem === "#") {
                    this.WALL[`${rowNum}-${colNum}`] = true;
                } else if (elem !== "." && elem !== "\r") {
                    const poi = {x: colNum, y: rowNum, elem};
                    this.POI.push(poi);
                    this.poiLocations[`${rowNum}-${colNum}`] = poi;
                }
            });
        });
    }

    public calculateDistances(): DistanceMatrix {
        const distanceMatrix: DistanceMatrix = {};
        for (const poi of this.POI) {
            distanceMatrix[poi.elem] = {};
            distanceMatrix[poi.elem][poi.elem] = 0;
            const queue = [[0, poi.y, poi.x]];
            const visited: Locations = {};
            const starthash = `${poi.y}-${poi.x}`;
            visited[starthash] = true;
            while (queue.length) {
                const [step, currentY, currentX] = queue.shift() || [ 0, -1, -1];
                if (currentX === -1) {
                    break;
                }
                for (const [plusX, plusY] of this.directions) {
                    const newX = currentX + plusX;
                    const newY = currentY + plusY;
                    const hash = `${newY}-${newX}`;
                    if (!(hash in visited) && !(`${newY}-${newX}` in this.WALL)) {
                        queue.push([step + 1, newY, newX]);
                        visited[hash] = true;
                        const foundpoi = this.poiLocations[hash];
                        if (foundpoi) {
                            distanceMatrix[poi.elem][foundpoi.elem] = step + 1;
                        }
                    }
                }
            }
        }
        return distanceMatrix;
    }

    public getShortestDistances(distanceMatrix: DistanceMatrix) {
        // 7! is not toooo much.
        const permuteArray = Array.from({length: Object.keys(distanceMatrix).length}, (_, i) => i);
        const permutations = permute(permuteArray);
        let cheapest = Number.MAX_VALUE;
        for (const permutation of permutations) {
            permutation.push(0);
            cheapest = Math.min(cheapest,
                permutation.reduce(
                ([prevElem, sum], elem) => [elem, sum + distanceMatrix[prevElem][elem]],
                [0, 0])[1]);
        }
        return cheapest;
    }
}

/**
 * Heap's method to generate all permutations of N in O(n!) time complexity,
 *
 * http://homepage.math.uiowa.edu/~goodman/22m150.dir/2007/Permutation%20Generation%20Methods.pdf
 */
function permute(permutation: number[]): number[][] {
    const length = permutation.length;
    const result = [permutation.slice()];
    const c = new Array(length).fill(0);
    let i = 1;
    let k;
    let p;

    while (i < length) {
        if (c[i] < i) {
            k = i % 2 && c[i];
            p = permutation[i];
            permutation[i] = permutation[k];
            permutation[k] = p;
            ++c[i];
            i = 1;
            result.push(permutation.slice());
        } else {
            c[i] = 0;
            ++i;
        }
    }
    return result;
}
