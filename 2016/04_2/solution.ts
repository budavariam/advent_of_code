export function solution(input: string[]) {
    return "" + input
        .map(parseInput)
        .filter((room) => room.isNorthPoleObject())
        .map((room) => room.sectorID);
}

const REGEXP = /([a-z\-]+)-(\d+)(?:\[(\w+)\])?/;
function parseInput(line: string): Room {
    const matches = line.match(REGEXP);
    if (matches) {
        const name = matches[1];
        const sectorID = parseInt(matches[2], 10);
        const checksum = matches[3];
        return new Room(name, sectorID, checksum);
    } else {
        return new Room("", 0, "filterthis");
    }
}

class Room {
    private histogram = {};
    private topfiveordered = "";
    private decipheredName = "";

    constructor(name: string, public readonly sectorID: number, private checksum: string) {
        this.histogram = this.calcHistogram(name);
        this.topfiveordered = this.calcChecksum(this.histogram);
        this.decipheredName = this.decipher(name, sectorID);
    }

    public toString() {
        return this.decipheredName;
    }

    public isValid() {
        return this.topfiveordered === this.checksum;
    }

    public isNorthPoleObject() {
        return this.decipheredName.indexOf("north") > -1;
    }

    private decipher(text: string, count: number) {
        const lowerCaseShift = "a".charCodeAt(0); // 97
        return String.fromCharCode(...text.split("").map((char) => {
            let shiftedChar = char.charCodeAt(0);
            if (shiftedChar === 45) {
                shiftedChar = 32; // ' '.charCodeAt(0);
            } else {
                shiftedChar -= lowerCaseShift;
                shiftedChar += count;
                shiftedChar %= 26;
                shiftedChar += lowerCaseShift;
            }
            return shiftedChar;
        }));
    }

    private calcHistogram(name: string): any {
        const hist: any = {};
        name.split("").forEach((character) => {
            if (character in hist) {
                hist[character] += 1;
            } else {
                hist[character] = 1;
            }
        });
        return hist;
    }

    private calcChecksum(histogram: any): string {
        return Object.keys(histogram).sort((left, right) => {
            if (((histogram[left] === histogram[right]) && (left > right)) || (histogram[left] < histogram[right])) {
                return 1;
            } else {
                return -1;
            }
        }).join("").slice(0, 5);
    }
}
