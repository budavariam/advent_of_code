
export function solution(input: string[], options?: any) {
    const startHash = input[0];
    const diskSize = options.diskSize;
    const randomDataGenerator = new DragonCurve(startHash, diskSize);
    return randomDataGenerator.checkSum();
}

class DragonCurve {
    constructor(
        private a: string,
        private readonly disksize: number,
    ) {}

    public checkSum() {
        let checksum = "";
        let data = this.generateData();
        do {
            checksum = "";
            for (let i = 0; i < data.length; i += 2 ) {
                checksum += (data[i] === data[i + 1]) ? "1" : "0";
            }
            data = checksum;
        } while (data.length % 2 === 0);
        return checksum;
    }

    private generateData() {
        let result = this.a;
        while (result.length < this.disksize) {
            result = this.next(result);
        }
        return result.slice(0, this.disksize);
    }

    private next(a: string) {
        const b = a
            .split("")
            .reverse()
            .map((value: string) => (value === "0" ? "1" : "0"))
            .join("");
        return `${a}0${b}`;
    }
}
