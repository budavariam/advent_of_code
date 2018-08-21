import { instructionFactory, Instruction } from "./InstructionFactory";

export function solution(input: string[], options?: any) {
    const generator = new PasswordGenerator(input, options.seed, true);
    return "" + generator.scramble();
}

class PasswordGenerator {
    private instructions: Instruction[] = [];

    constructor(input: string[], private current: string = "", reverse: boolean = false) {
        if (reverse) {
            input = input.reverse();
        }
        for (const line of input) {
            this.instructions.push(instructionFactory(line, reverse));
        }
    }

    public scramble() {
        for (const instruction of this.instructions) {
            this.current = instruction.operate(this.current);
            // console.log(instruction.toString());
            // console.log(this.current);
        }
        return this.current;
    }
}
