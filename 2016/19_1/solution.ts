export function solution(input: string[], options?: any) {
    const first: Elf = new Elf(1);
    let prevElf: Elf = first;
    const playerNumber = parseInt(input[0], 10);
    for (let i = 2; i <= playerNumber; i++) {
        const nextElf = new Elf(i);
        prevElf.leftNeighbour = nextElf;
        prevElf = nextElf;
    }
    prevElf.leftNeighbour = first;
    return "" + playWhiteElephant(first).id;
}

class Elf {
    public leftNeighbour: Elf | null = null;
    constructor(public readonly id: number) {}
}

function playWhiteElephant(elves: Elf): Elf {
    let current: Elf = elves;
    while (current.leftNeighbour !== current) {
        if (current.leftNeighbour) {
            current.leftNeighbour = current.leftNeighbour.leftNeighbour;
            current = current.leftNeighbour ? current.leftNeighbour : new Elf(-1);
        }
    }
    return current;
}
