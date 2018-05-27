import { InstructionFactory } from "./instructionFactory";

export function solution(input: string[]) {
    const screen = new Screen();
    screen.instructions(input);
    return "" + screen.litPixels;
}
export class Screen {
    public litPixels = 0;
    private matrix: boolean[][] = [];
    private debug = false;

    constructor(
        startState = false,
        private width: number = 50,
        private height = 6,
    ) {
        this.matrix = this.initMatrix(width, height, startState);
    }

    public instructions(input: string[]) {
        input.forEach((line) => {
            const instructionName = line.split(" ")[0];
            if (this.debug) {console.log(line); }
            if (instructionName === "rotate" || instructionName === "rect") {
                const instruction = InstructionFactory.getInstruction(instructionName, line, this.width, this.height);
                instruction.operate(this.matrix);
                if (this.debug) {
                    this.litPixels = this.countLitPiexels();
                    this.printScreen();
                    console.log(`${this.litPixels} pixel is lit`);
                }
            } else {
                console.error("Missing instruction!");
            }
        });
        this.litPixels = this.countLitPiexels();
    }

    public printScreen() {
        for (const line of this.matrix) {
            console.log(line.map((char) => char ? "#" : ".").join(""));
        }
        console.log();
    }

    private initMatrix(width: number, height: number, startState: boolean) {
        const newMatrix: boolean[][] = [];
        for (let row = 0; row < height; row++) {
            const line = [];
            for (let col = 0; col < width; col++) {
                line.push(startState ? true : false);
            }
            newMatrix.push(line);
        }
        return newMatrix;
    }

    private countLitPiexels() {
        return this.matrix.reduce((result, line) => result + line.filter((elem) => elem === true).length, 0);
    }
}
