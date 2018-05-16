export function solution(input: string[]) {
    return "" + input
        .map(parseInput)
        .filter((room: Room) => room.isValid())
        .reduce((acc: number, curr: Room) => acc += curr.sectorID, 0);
}

const REGEXP = /([a-z\-]+)-(\d+)(?:\[(\w+)\])?/;
function parseInput(line: string): Room {
    const matches = line.match(REGEXP);
    if (matches) {
        return new Room(matches[1].replace(/-/g, ""), parseInt(matches[2], 10), matches[3]);
    } else {
        return new Room("", 0, "filterthis");
    }
}

class Room {
    private histogram = {};
    private topfiveordered = "";

    constructor(name: string, public readonly sectorID: number, private checksum: string) {
        this.histogram = this.calcHistogram(name);
        this.topfiveordered = this.calcChecksum(this.histogram);
    }

    public isValid() {
        return this.topfiveordered === this.checksum;
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
