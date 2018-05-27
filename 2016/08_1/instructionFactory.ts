abstract class Instruction {
    public abstract operate(matrix: boolean[][]): void;
}

class Rotate extends Instruction {
    private regex = /rotate (row|column) (?:x|y)=(\d+) by (\d+)/;

    private isRow = false;
    private startFrom = 0;
    private rotateBy = 0;

    constructor(line: string, screenWidth: number, private screenHeight: number) {
        super();
        const match = line.match(this.regex);
        if (match) {
            this.isRow = match[1] === "row";
            this.startFrom = parseInt(match[2], 10);
            this.rotateBy = parseInt(match[3], 10);
        }
    }

    public operate(matrix: boolean[][]) {
        if (this.isRow) {
            this.rotateRow(matrix);
        } else {
            this.rotateCol(matrix);
        }
    }

    private rotate(array: boolean[]) {
        const rotateHalf = array.length - this.rotateBy;
        const firstHalf = array.slice(0, rotateHalf);
        const secondHalf = array.slice(rotateHalf, array.length);
        return secondHalf.concat(firstHalf);
    }

    private rotateRow(matrix: boolean[][]) {
        matrix[this.startFrom] = this.rotate(matrix[this.startFrom]);
    }

    private rotateCol(matrix: boolean[][]) {
        const startCol = matrix.map((line) => line[this.startFrom]);
        const rotated = this.rotate(startCol);
        for (let col = 0; col < this.screenHeight; col++) {
            matrix[col][this.startFrom] = rotated[col];
        }
    }
}

class Rect extends Instruction {
    private regex = /rect (\d+)x(\d+)/;

    private width = 0;
    private height = 0;

    constructor(line: string, screenWidth: number, screenHeight: number) {
        super();
        const match = line.match(this.regex);
        if (match) {
            this.width = parseInt(match[1], 10);
            this.height = parseInt(match[2], 10);
        }
    }
    public operate(matrix: boolean[][]) {
        for (let row = 0; row < this.height; row++) {
            for (let col = 0; col < this.width; col++) {
                matrix[row][col] = true;
            }
        }
    }
}

export class InstructionFactory {
    public static getInstruction(name: "rotate"|"rect", line: string, width: number, height: number): Instruction {
        return new (InstructionFactory.instrClasses[name])(line, width, height);
    }

    private static instrClasses: {
            rotate: typeof Rotate,
            rect: typeof Rect,
        } = {
        rotate: Rotate,
        rect: Rect,
    };
}
