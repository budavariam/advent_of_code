export function solution(input: string[]) {
    const keypad = new Keypad(Key.K5);
    const keycodes: string[] = input
        .map((path: string) => keypad.processPath(path));
    return keycodes.reduce((accumulate, current) => accumulate + current);
}

enum Key {
    K1= 1, K2, K3, K4, K5, K6, K7, K8, K9, KA = "A", KB = "B", KC = "C", KD = "D",
}

interface IKeyLookup {
    [key: string]: { [direction: string]: Key | null};
}

/*
    1
  2 3 4
5 6 7 8 9
  A B C
    D
*/

const nextKey: IKeyLookup = {
    K1: {U: null, D: Key.K3, L: null, R: null},
    K2: {U: null, D: Key.K6, L: null, R: Key.K3},
    K3: {U: Key.K1, D: Key.K7, L: Key.K2, R: Key.K4},
    K4: {U: null, D: Key.K8, L: Key.K3, R: null},
    K5: {U: null, D: null, L: null, R: Key.K6},
    K6: {U: Key.K2, D: Key.KA, L: Key.K5, R: Key.K7},
    K7: {U: Key.K3, D: Key.KB, L: Key.K6, R: Key.K8},
    K8: {U: Key.K4, D: Key.KC, L: Key.K7, R: Key.K9},
    K9: {U: null, D: null, L: Key.K8, R: null},
    KA: {U: Key.K6, D: null, L: null, R: Key.KB},
    KB: {U: Key.K7, D: Key.KD, L: Key.KA, R: Key.KC},
    KC: {U: Key.K8, D: null, L: Key.KB, R: null},
    KD: {U: Key.KB, D: null, L: null, R: null},
};

class Keypad {
    constructor(
        private startPosition: Key,
    ) {}

    public processPath(rawData: string): string {
        const path = rawData.split("");
        let lastPath: Key = this.startPosition;
        for (const current of path) {
            const next: Key | null = nextKey[`K${lastPath.toString()}`][current];
            if (next) {
                lastPath = next;
            }
        }
        this.startPosition = lastPath;
        return "" + lastPath;
    }
}
