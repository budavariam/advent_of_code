export function solution(input: string[], options?: any) {
    const machine = new Machine();
    machine.loadCode(input);
    machine.runCode();
    return "" + machine.getRegister("a");
}

type AvailableRegisters = "a"|"b"|"c"|"d";

type IRegister = {
    [r in AvailableRegisters]: number
};

interface Instruction {
    operate(instructionPointer: number, registers: IRegister): [number, IRegister];
}

class Machine {
    constructor(
        private registers: IRegister = {a: 0, b: 0, c: 0, d: 0},
        private debug = false,
        private IP = 0,
        private instructions: Instruction[] = [],
    ) {}

    public loadCode(assembunnyInstructions: string[]) {
        this.instructions = assembunnyInstructions.map((instr) => {
            return InstructionFactory.parseLine(instr);
        });
    }

    public runCode() {
        const instructionCount = this.instructions.length;
        while (this.IP < instructionCount && this.IP >= 0) {
            [this.IP, this.registers] = this.instructions[this.IP].operate(this.IP, this.registers);
            if (this.debug) {
                console.log(this.IP, this.registers);
            }
        }
    }

    public getRegister(register: AvailableRegisters): number {
        return this.registers[register];
    }
}

class InstructionFactory {
    public static parseLine(line: string) {
        const [name, ...params] = line.trim().split(" ");
        switch (name) {
            case "jnz":
                return new JNZ(this.getNumberOrRegister(params[0]), parseInt(params[1], 10));
            case "cpy":
                return new CPY(this.getNumberOrRegister(params[0]), this.getRegister(params[1]));
            case "inc":
                return new INC(this.getRegister(params[0]));
            case "dec":
                return new DEC(this.getRegister(params[0]));
            default:
                throw new Error(`PARSE ERROR on line: ${line}`);
        }
    }

    public static getRegister(rawData: string): AvailableRegisters {
        if (rawData === "a" ||
            rawData === "b" ||
            rawData === "c" ||
            rawData === "d") {
            return rawData;
        } else {
            throw new Error(`Can not parse register ${rawData}`);
        }
    }

    public static getNumberOrRegister(rawData: string): number | AvailableRegisters {
        const parsedNumber = parseInt(rawData, 10);
        if (isNaN(parsedNumber)) {
            return this.getRegister(rawData);
        } else {
            return parsedNumber;
        }
    }
}

class INC implements Instruction {
    constructor(
        private registerName: AvailableRegisters,
    ) {}

    public operate(IP: number, registers: IRegister): [number, IRegister] {
        registers[this.registerName] += 1;
        return [IP + 1, registers];
    }
}

class DEC implements Instruction {
    constructor(
        private registerName: AvailableRegisters,
    ) {}

    public operate(IP: number, registers: IRegister): [number, IRegister] {
        registers[this.registerName] -= 1;
        return [IP + 1, registers];
    }
}

class CPY implements Instruction {
    constructor(
        private copyValue: number | AvailableRegisters,
        private registerName: AvailableRegisters,
    ) {}

    public operate(IP: number, registers: IRegister): [number, IRegister] {
        let put: number = 0;
        if (typeof this.copyValue === "number") {
            put = this.copyValue;
        } else {
            put = registers[this.copyValue];
        }
        registers[this.registerName] = put;
        return [IP + 1, registers];
    }
}

class JNZ implements Instruction {
    constructor(
        private checkValue: number | AvailableRegisters,
        private jumpCount: number,
    ) {}

    public operate(IP: number, registers: IRegister): [number, IRegister] {
        let jump: number = 0;
        if (typeof this.checkValue === "number") {
            jump = this.checkValue ? this.jumpCount : 1;
        } else {
            const check = registers[this.checkValue];
            jump = (check) ? this.jumpCount : 1;
        }
        return [IP + jump, registers];
    }
}
