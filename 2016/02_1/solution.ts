export function solution(input: string[]) {
    const keypad = new Keypad(Key.K5);
    const keycodes: string[] = input
        .map((path: string) => keypad.processPath(path));
    return "" + keycodes.reduce((accumulate, current) => accumulate + current);
}

enum Key {
    K1= 1, K2, K3, K4, K5, K6, K7, K8, K9,
}

interface IKeyLookup {
    [key: string]: { [direction: string]: Key | null};
}

const nextKey: IKeyLookup = {
    K1: {U: null, D: Key.K4, L: null, R: Key.K2},
    K2: {U: null, D: Key.K5, L: Key.K1, R: Key.K3},
    K3: {U: null, D: Key.K6, L: Key.K2, R: null},
    K4: {U: Key.K1, D: Key.K7, L: null, R: Key.K5},
    K5: {U: Key.K2, D: Key.K8, L: Key.K4, R: Key.K6},
    K6: {U: Key.K3, D: Key.K9, L: Key.K5, R: null},
    K7: {U: Key.K4, D: null, L: null, R: Key.K8},
    K8: {U: Key.K5, D: null, L: Key.K7, R: Key.K9},
    K9: {U: Key.K6, D: null, L: Key.K8, R: null},
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
