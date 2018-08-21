export function instructionFactory(line: string, reverse: boolean): Instruction {
    for (const instruction of instrClasses) {
        const result = instruction.check(line, reverse);
        if (result) {
            return result;
        }
    }
    return new NoOp();
}

export abstract class Instruction {
    public static check(line: string, reverse: boolean): Instruction | null { return null; }
    public abstract operate(current: string): string;
}

class NoOp extends Instruction {
    public static check(_: string, __: boolean): Instruction | null {
        return null;
    }

    public operate(current: string): string {
        return current;
    }
}

class SwapPosition extends Instruction {
    public static check(line: string, reverse: boolean): Instruction | null {
        const match = line.match(/swap position (\d+) with position (\d+)/);
        if (match) {
            let [p1, p2] = [parseInt(match[1], 10), parseInt(match[2], 10)];
            if (reverse) {
                [p1, p2] = [p2, p1];
            }
            return new SwapPosition(p1, p2);
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

    public toString() {
        return `SwapPosition ${this.pos1} - ${this.pos2}`;
    }
}

class SwapLetter extends Instruction {
    public static check(line: string, reverse: boolean): Instruction | null {
        const match = line.match(/swap letter (\w) with letter (\w)/);
        if (match) {
            let [l1, l2] = [match[1], match[2]];
            if (reverse) {
                [l1, l2] = [l2, l1];
            }
            return new SwapLetter(l1, l2);
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

    public toString() {
        return `SwapLetter ${this.char1} - ${this.char2}`;
    }
}

class RotateDirection extends Instruction {
    public static check(line: string, reverse: boolean): Instruction | null {
        const match = line.match(/rotate (left|right) (\d+) steps?/);
        if (match) {
            let direction = match[1];
            if (reverse) {
                direction = (direction === "left") ? "right" : "left";
            }
            return new RotateDirection(direction, parseInt(match[2], 10));
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

    public toString() {
        return `RotateDirection ${this.direction} - ${this.count}`;
    }
}

class Rotate extends Instruction {
    public static check(line: string, reverse: boolean): Instruction | null {
        const match = line.match(/rotate based on position of letter (\w)/);
        if (match) {
            return new Rotate(match[1], reverse);
        } else {
            return null;
        }
    }

    constructor(private letter: string, private reverse = false) {
        super();
    }

    public operate(current: string): string {
        if (this.reverse) {
            const index = current.indexOf(this.letter) || 8; // init 0 for 8.
            // I've figured out a reverse pattern in paper.
            const reverseIndex = (index % 2 === 0) ? ((index + current.length - 2) / 2) : (index - 1) / 2;
            const diff = reverseIndex - index;
            const rotator = new RotateDirection(diff > 0 ? "right" : "left", Math.abs(diff));
            return rotator.operate(current);
        } else {
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

    public toString() {
        return `Rotate ${this.letter}`;
    }
}

class Reverse extends Instruction {
    public static check(line: string, _: boolean): Instruction | null {
        const match = line.match(/reverse positions (\d+) through (\d+)/);
        // this should be the same function on reverse also.
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

    public toString() {
        return `Reverse ${this.from} - ${this.to}`;
    }
}

class Move extends Instruction {
    public static check(line: string, reverse: boolean): Instruction | null {
        const match = line.match(/move position (\d+) to position (\d+)/);
        if (match) {
            let [p1, p2] = [parseInt(match[1], 10), parseInt(match[2], 10)];
            if (reverse) {
                [p1, p2] = [p2, p1];
            }
            return new Move(p1, p2);
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

    public toString() {
        return `Move ${this.from} - ${this.to}`;
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
