
import { MD5 } from "crypto-js";

export function solution(input: string[], options?: any) {
    const vault = new Vault(4, 4);
    return vault.findShortestPath(input[0], [0, 0], [3, 3]);
}

type Directions = { [k in string]: [number, number] };

const directions: Directions = {
    U: [0, -1],
    D: [0, 1],
    L: [-1, 0],
    R: [1, 0],
};

type Position = [number, number];
function samePosition(posA: Position, posB: Position) {
    return posA[0] === posB[0] && posA[1] === posB[1];
}

function changePosition(posA: Position, posB: Position): [number, number] {
    return [posA[0] + posB[0], posA[1] + posB[1]];
}

interface IPath {
    position: Position;
    path: string;
}

class Vault {
    private queue: IPath[] = [];
    private doorOrder = ["U", "D", "L", "R"];
    constructor(
        private row: number,
        private col: number) {
    }

    public findShortestPath(code: string, start: Position, end: Position): string {
        this.queue.push({ path: "", position: start });
        while (this.queue.length) {
            const prevPath: IPath | undefined = this.queue.shift();
            if (!prevPath) {
                console.error("Path missing");
                continue;
            }
            const hash = MD5(code + prevPath.path).toString();
            const doors = this.getOpenDoorDirections(hash.slice(0, 4), prevPath.position);
            for (const direction of doors) {
                const newPath = prevPath.path + direction;
                const newPosition = changePosition(prevPath.position, directions[direction]);
                if (samePosition(newPosition, end)) {
                    return newPath;
                }
                this.queue.push({ path: newPath, position: newPosition });
            }
        }
        return "NOT_FOUND";
    }

    private isNotWall(pos: Position) {
        return pos[0] >= 0 && pos[0] < this.col && pos[1] >= 0 && pos[1] < this.row;
    }

    private getOpenDoorDirections(door: string, pos: Position): string[] {
        return this.doorOrder.filter((elem, i) =>
            this.isNotWall(changePosition(pos, directions[elem])) &&
            door[i].match(/[bcdef]/));
    }
}
