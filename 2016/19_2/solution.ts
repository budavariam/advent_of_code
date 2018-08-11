export function solution(input: string[], options?: any) {
    const first: Elf = new Elf(1);
    let prevElf: Elf = first;
    let otherHalf: Elf = first; // this will be overwritten during initialization
    const playerNumber = parseInt(input[0], 10);
    const halfGroupCount = Math.floor(playerNumber / 2);
    for (let i = 2; i <= playerNumber; i++) {
        const nextElf = new Elf(i);
        prevElf.leftNeighbour = nextElf;
        prevElf = nextElf;
        if (halfGroupCount === i) {
            otherHalf = nextElf;
        }
    }
    prevElf.leftNeighbour = first;
    return "" + playWhiteElephant(first, otherHalf, playerNumber);
}

class Elf {
    public leftNeighbour: Elf;
    constructor(public readonly id: number) {
        this.leftNeighbour = this; // this will be overwritten by the end of initialization
    }
}

function playWhiteElephant(current: Elf, swapWith: Elf, elfCount: number): number {
    while (current.leftNeighbour !== current) {
        current = current.leftNeighbour;
        swapWith.leftNeighbour = swapWith.leftNeighbour.leftNeighbour;
        if (elfCount-- % 2 === 1) {
            swapWith = swapWith.leftNeighbour;
        }
    }
    return current.id;
}
