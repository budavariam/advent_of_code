export function solution(input: string[]) {
    return "" + input
        .map((line) => new IPv7(line))
        .filter((ip) => ip.supportsTLS)
        .length;
}

class IPv7 {
    public supportsTLS = false;

    private bracketed: ABA[] = [];
    private outOfBracket: ABA[] = [];

    constructor(line: string) {
        this.parse(line);
        this.supportsTLS = this.checkBAB();
    }

    public parse(line: string) {
        let inBracket = false;
        let lastBracketIndex = -1;

        for (let i = 0; i < line.length; i++) {
            if (line[i] === "[" || line[i] === "]") {
                inBracket = !inBracket;
                lastBracketIndex = i;
            } else if (i < 2) {
                continue;
            } else if ((lastBracketIndex === -1 || (i - lastBracketIndex) > 2) &&
                      line[i - 2] === line[i] && line[i] !== line[i - 1]) {
                const aba = new ABA(line[i], line[i - 1]);
                if (inBracket) {
                    this.bracketed.push(aba);
                } else {
                    this.outOfBracket.push(aba);
                }
            }
        }
    }

    private checkBAB(): boolean {
        return this.outOfBracket.length > 0 &&
            this.outOfBracket.some((aba) => this.bracketed.some((bab) => aba.checkBAB(bab)));
    }
}

class ABA {
    constructor(public double: string, public single: string) {}
    public checkBAB(bab: ABA): boolean {
        return this.single === bab.double && this.double === bab.single;
    }
}
