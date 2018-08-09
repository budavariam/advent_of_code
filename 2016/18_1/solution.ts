export function solution(input: string[], options?: any) {
    const room = new TrapRoom(input[0]);
    room.buildMap(options.count);
    return "" + room.countEmptySlots();
}

class TrapRoom {
    private map: string[] = [];
    private lineLength: number = -1;

    constructor(private firstRow: string) {
        this.lineLength = firstRow.length;
        this.map.push(firstRow);
    }

    public buildMap(size: number): void {
        let prevRow = this.firstRow;
        for (let i = 0; i < size - 1; i++ ) {
            const currentRow = this.processRow(prevRow);
            prevRow = currentRow;
            this.map.push(currentRow);
        }
        // console.log(this.map);
    }

    public countEmptySlots(): number {
        return this.map.reduce(
            (acc, line) => acc + line.split("").reduce(
                (freecount, char) => freecount + ((char === ".") ? 1 : 0),
                0),
            0);
    }

    private processRow(row: string): string {
        return row.split("").map((value, i, arr) => {
            // true if it is a trap.
            const left: boolean = (i === 0) ? false : arr[i - 1] === "^";
            const center: boolean = value === "^";
            const right: boolean = (i === this.lineLength - 1) ? false : arr[i + 1] === "^";
            /*
            Its left and center tiles are traps, but its right tile is not.
            Its center and right tiles are traps, but its left tile is not.
            Only its left tile is a trap.
            Only its right tile is a trap.
            */
            return left  && center  && !right ||
                   !left && center  && right  ||
                   left  && !center && !right ||
                   !left && !center && right ? "^" : ".";
        }).join("");
    }
}
