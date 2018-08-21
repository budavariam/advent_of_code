export function instructionFactory(line: string): Instruction {
    for (const instruction of instrClasses) {
        const result = instruction.check(line);
        if (result) {
            return result;
        }
    }
    return new NoOp();
}

export abstract class Instruction {
    public static check(_: string): Instruction | null { return null; }
    public abstract operate(current: string): string;
}

class NoOp extends Instruction {
    public static check(_: string): Instruction | null {
        return null;
    }

    public operate(current: string): string {
        return current;
    }
}

class SwapPosition extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/swap position (\d+) with position (\d+)/);
        if (match) {
            return new SwapPosition(parseInt(match[1], 10), parseInt(match[2], 10));
        } else {
            return null;
        }
    }

    constructor(private pos1: number, private pos2: number) {
        super();
        if (this.pos2 < this.pos1) {
            [this.pos1, this.pos2] = [this.pos2, this.pos1];
        }
    }

    public operate(current: string): string {
        const [ch1, ch2] = [current[this.pos1], current[this.pos2]];
        return current.substr(0, this.pos1) +
            ch2 +
            current.substring(this.pos1 + 1, this.pos2) +
            ch1 +
            current.substr(this.pos2 + 1);
    }
}

class SwapLetter extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/swap letter (\w) with letter (\w)/);
        if (match) {
            return new SwapLetter(match[1], match[2]);
        } else {
            return null;
        }
    }

    constructor(private char1: string, private char2: string) {
        super();
    }

    public operate(current: string): string {
        return current
            .split("")
            .map((char) => (char === this.char1) ? (this.char2) : (char === this.char2) ? this.char1 : char)
            .join("");
    }
}

class RotateDirection extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/rotate (left|right) (\d+) steps?/);
        if (match) {
            return new RotateDirection(match[1], parseInt(match[2], 10));
        } else {
            return null;
        }
    }

    constructor(private direction: string, private count: number) {
        super();
    }

    public operate(current: string): string {
        this.count %= current.length;
        if (this.count === 0) {
            return current;
        } else if (this.direction === "left") {
            return current.substring(this.count) + current.substring(0, this.count);
        } else {
            return current.substr(-this.count) + current.substr(0, current.length - this.count);
        }
    }
}

class Rotate extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/rotate based on position of letter (\w)/);
        if (match) {
            return new Rotate(match[1]);
        } else {
            return null;
        }
    }

    constructor(private letter: string) {
        super();
    }

    public operate(current: string): string {
        /*
        rotate based on position of letter X means that the whole string
        should be rotated to the right based on the index of letter X
        (counting from 0) as determined before this instruction does
        any rotations. Once the index is determined, rotate the string
        to the right one time, plus a number of times equal to that
        index, plus one additional time if the index was at least 4.
        */
        const index = current.indexOf(this.letter);
        const rotator = new RotateDirection("right", index + ((index >= 4) ? 2 : 1));
        return rotator.operate(current);
    }
}

class Reverse extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/reverse positions (\d+) through (\d+)/);
        if (match) {
            return new Reverse(parseInt(match[1], 10), parseInt(match[2], 10));
        } else {
            return null;
        }
    }

    constructor(private from: number, private to: number) {
        super();
        if (this.from > this.to) {
            [this.from, this.to] = [this.to, this.from];
        }
    }

    public operate(current: string): string {

        return current.substr(0, this.from) +
            current.substring(this.from, this.to + 1).split("").reverse().join("") +
            current.substring(this.to + 1);
    }
}

class Move extends Instruction {
    public static check(line: string): Instruction | null {
        const match = line.match(/move position (\d+) to position (\d+)/);
        if (match) {
            return new Move(parseInt(match[1], 10), parseInt(match[2], 10));
        } else {
            return null;
        }
    }

    constructor(private from: number, private to: number) {
        super();
    }

    public operate(current: string): string {
        const charToInsert = current.charAt(this.from);
        if (this.from < this.to) {
            return current.substring(0, this.from) +
                current.substring(this.from + 1, this.to + 1) +
                charToInsert +
                current.substring(this.to + 1);
        } else {
            return current.substring(0, this.to) +
                charToInsert +
                current.substring(this.to, this.from) +
                current.substring(this.from + 1);
        }
    }
}

const instrClasses = [
    SwapPosition,
    SwapLetter,
    RotateDirection,
    Rotate,
    Reverse,
    Move,
];
