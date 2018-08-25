export function solution(input: string[], options?: any) {
    const cluster = new Cluster();
    cluster.parseNodes(input.slice(2));
    const map = cluster.generateMap();
    cluster.printNodes(map);
    return "" + cluster.countLeastMoves(map);
}

interface IPosition {
    x: number;
    y: number;
}

class Cluster {
    private usedNodes: Node[] = [];
    private availstarts: {[s in string]: number} = {};
    private availWhereis: {[s in string]: number} = {};
    private highestX: number = -1;
    private highestY: number = -1;
    private averageSize: number = 0;
    private emptyNodePos: IPosition = {x: -1, y: -1};

    public parseNodes(lines: string[]) {
        const nodes = [];
        for (const line of lines) {
            nodes.push(new Node(line));
        }
        this.fillNodeArrays(nodes);
    }

    public generateMap() {
        const map: Node[][] = [];
        for (const node of this.usedNodes) {
            if (!(node.y in map)) {
                map[node.y] = [];
            }
            let sign = "";
            if (node.y === 0 && node.x === 0) {
                sign = "(.)";
            } else if (node.y === 0 && node.x === this.highestX) {
                sign = " G ";
            } else if (node.used === 0) {
                sign = " _ ";
            } else if (node.used >= this.averageSize) {
                sign = ` # `;
                node.block = true;
            } else {
                sign = " . ";
            }
            node.sign = sign;
            map[node.y][node.x] = node;
        }
        return map;
    }

    public printNodes(map: Node[][]) {
        console.log(map.map((line) => line.join("")).join("\n"));
    }

    public countLeastMoves(map: Node[][]) {
        // Move the empty spot next to the moveable data.
        const stepFromEmpty = this.getShortestStepCount(map, this.emptyNodePos, {y: 0, x: this.highestX - 1});
        // Assume that there is no blockage between the data and the accessable node. And the row below.
        const distancebetweenMoveableAndAccessible = this.highestX - 1;
        // Move the empty spot around the data takes 5 steps: Move to the G position, down, left, left, up
        // Move the data to the accessible spot, when the distance is only one.
        return stepFromEmpty +
            (distancebetweenMoveableAndAccessible * 5) +
            1;
    }

    private getShortestStepCount(map: Node[][], from: IPosition, to: IPosition) {
        const queue: [number, Node][] = [[0, map[from.y][from.x]]];
        const visited: {[x in string]: boolean} = {};
        while (true) {
            const [step, current] = queue.shift() || [0, undefined];
            if (current) {
                if (visited[`${current.y}-${current.x}`]) {
                    continue;
                }
                if (current.isEqualPosition(to)) {
                    return step;
                }
                visited[`${current.y}-${current.x}`] = true;
                if (current.y - 1 >= 0 && !(`${current.y - 1}-${current.x}` in visited)) {
                    const up = map[current.y - 1][current.x];
                    if (!up.block) {
                        queue.push([step + 1, up]);
                    }
                }
                if (current.y + 1 <= this.highestY && !(`${current.y + 1}-${current.x}` in visited)) {
                    const down = map[current.y + 1][current.x];
                    if (!down.block) {
                        queue.push([step + 1, down]);
                    }
                }
                if (current.x + 1 <= this.highestX && !(`${current.y}-${current.x + 1}` in visited)) {
                    const right = map[current.y][current.x + 1];
                    if (!right.block) {
                        queue.push([step + 1, right]);
                    }
                }
                if (current.x - 1 >= 0 && !(`${current.y}-${current.x - 1}` in visited)) {
                    const left = map[current.y][current.x - 1];
                    if (!left.block) {
                        queue.push([step + 1, left]);
                    }
                }
            } else {
                break;
            }
        }
        return 0;
    }

    private fillNodeArrays(nodes: Node[]): void {

        this.usedNodes = nodes
            .slice()
            .sort((nodeA, nodeB) => nodeB.used - nodeA.used);
            // descending order by used space

        nodes.sort((nodeA, nodeB) => nodeA.avail - nodeB.avail)
            // ascending order by available space
            .forEach((node, index) => {
                if (!(node.avail in this.availstarts)) {this.availstarts[node.avail] = index; }
                this.availWhereis[node.filesystem] = index;
                if (this.highestX < node.x && node.y === 0) {
                    this.highestX = node.x;
                }
                this.highestY = Math.max(this.highestY, node.y);
                this.averageSize += node.size;
                if (node.used === 0) {
                    this.emptyNodePos = node.getPosition();
                }
        });
        // Get the average size to determine the large and useless nodes that act as blockers.
        this.averageSize /= nodes.length;
        // fill the missing parts from the hash table in order to be able to query fast.
        let prevAvail = -1;
        for (let index = this.usedNodes[0].used; index >= 0; index--) {
            if (index in this.availstarts) {
                prevAvail = this.availstarts[index];
            } else {
                this.availstarts[index] = prevAvail;
            }
        }
    }
}

class Node {
    public readonly x: number = -1;
    public readonly y: number = -1;
    public readonly filesystem: string = "";
    public readonly used: number = -1;
    public readonly avail: number = -1;
    public readonly size: number = -1;
    public readonly useperc: number = -1;
    public sign: string = " ";
    public block: boolean = false;

    constructor(line: string) {
        const matches = line.match(/x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%/);
        if (matches) {
            this.x = parseInt(matches[1], 10);
            this.y = parseInt(matches[2], 10);
            this.filesystem = `x${this.x}-y${this.y}`;
            this.size = parseInt(matches[3], 10);
            this.used = parseInt(matches[4], 10);
            this.avail = parseInt(matches[5], 10);
            this.useperc = parseInt(matches[6], 10);
        }
    }

    public toString() {
        return this.sign;
        // return `${this.used}/${this.size}`;
    }

    public getPosition(): IPosition {
        return {x: this.x, y: this.y};
    }

    public isEqualPosition(other: IPosition) {
        return this.x === other.x && this.y === other.y;
    }
}
