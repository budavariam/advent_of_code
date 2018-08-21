import { instructionFactory, Instruction } from "./InstructionFactory";

export function solution(input: string[], options?: any) {
    const generator = new PasswordGenerator(input);
    return "" + generator.scramble(options.seed);
}

class PasswordGenerator {
    private instructions: Instruction[] = [];

    constructor(input: string[], private current: string = "") {
        for (const line of input) {
            this.instructions.push(instructionFactory(line));
        }
    }

    public scramble(seed: string) {
        this.current = seed;
        for (const instruction of this.instructions) {
            this.current = instruction.operate(this.current);
        }
        return this.current;
    }
}
