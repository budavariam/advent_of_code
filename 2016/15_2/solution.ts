
export function solution(input: string[], options?: any) {
    const disks = new DiskContainer();
    disks.parseInput(input);
    return "" + disks.calculateTiming();
}

class DiskContainer {
    private disks: number[][] = [];
    private readonly regex = /Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)./;
    constructor() {}

    public parseInput(input: string[]) {
        this.disks = input
            .map((line: string) => (line.match(this.regex) || []).slice(1)
                .map((indexes) => parseInt(indexes, 10)));
        this.disks.push([this.disks[this.disks.length - 1][0] + 1, 11, 0]);
    }

    public calculateTiming() {
        const crinput: [number, number][] = [];
        for (const [id, positions, start] of this.disks) {
            crinput.push([positions, positions - ((id + start) % positions)]);
        }
        return this.chineseRemainder(crinput);
    }

    /**
     * I adjusted it from python version:
     * https://rosettacode.org/wiki/Chinese_remainder_theorem
     */
    private chineseRemainder(n: [number, number][]) {
        let sum = 0;
        const prod = n.reduce((acc, [curr, _]) => acc * curr, 1);

        for (const [moduloIndex, aIndex] of n) {
            const p = prod / moduloIndex;
            sum += aIndex * this.mulInv(p, moduloIndex) * p;
        }
        return sum % prod;
    }

    private mulInv(a: number, b: number) {
        const b0 = b;
        let [x0, x1] = [0, 1];
        if (b === 1) {
            return 1;
        }
        while (a > 1) {
            const q = Math.floor(a / b);
            [a, b] = [b, a % b];
            [x0, x1] = [x1 - q * x0, x0];
        }
        if (x1 < 0) {
            x1 += b0;
        }
        return x1;
    }
}
