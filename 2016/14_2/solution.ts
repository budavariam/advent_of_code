import { MD5 } from "crypto-js";

export function solution(input: string[], options?: any) {
    const startHash = input[0];
    const keygenerator = new KeyGenerator(startHash);
    keygenerator.prepareStream();
    let lastKeyIndex = 0;
    let keyCount = 0;
    while (keyCount < 64) {
        lastKeyIndex = keygenerator.next();
        keyCount++;
        console.log(keyCount, lastKeyIndex);
    }
    return "" + lastKeyIndex;
}

type Marks = {[k in string]: number};

class KeyGenerator {
    private quintetCount: Marks = {};
    private stream: [number, string, Set<string>][] = [];
    private lastHashIndex = 0;

    constructor(
        private readonly startHash: string,
    ) {}

    public prepareStream(initCount: number = 1000) {
        for (let i = 0; i < initCount; i++) {
            this.parseNextHash();
        }
    }

    public next() {
        while (true) {
            const [id, key, quintet] = this.stream.shift() || [0, "", new Set<string>()];
            this.shiftQuintets(quintet);
            this.parseNextHash();
            if (key && this.appearsInFollowingHashes(key)) {
                return id;
            }
        }
    }

    private stretchHash(hash: string, times: number) {
        for (let i = 0; i < times; i++) {
            hash = MD5(hash).toString();
        }
        return hash;
    }

    private parseNextHash() {
        const currentHash = this.stretchHash(this.startHash + this.lastHashIndex, 2017);
        const [key, allQuintets] = new HashParserAutomation(currentHash).parse();
        this.stream.push([this.lastHashIndex, key[0], allQuintets]);
        this.markQuintets(allQuintets);
        this.lastHashIndex++;
    }

    private appearsInFollowingHashes(triplet: string): boolean {
        return triplet in this.quintetCount ? this.quintetCount[triplet] !== 0 : false;
    }

    private markQuintets(quintets: Set<string>) {
        quintets.forEach((elem: string) => {
            this.quintetCount[elem] = elem in this.quintetCount ? this.quintetCount[elem] + 1 : 1;
        });
    }

    private shiftQuintets(quintets: Set<string>) {
        quintets.forEach((elem: string) => {
            this.quintetCount[elem]--; // there must be as many elems coming out as we put in.
        });
    }
}

class HashParserAutomation {
    private lastChar = "";
    private streak = 1;
    private firstTriplet = "";
    private quintets = new Set<string>();

    constructor(private hash: string) {}

    public parse(): [string, Set<string>] {
        for (const char of this.hash) {
            if (char === this.lastChar) {
                this.streak++;
                if (this.streak === 3 && !this.firstTriplet) {
                    this.firstTriplet = this.lastChar;
                } else if (this.streak === 5) {
                    this.quintets.add(this.lastChar);
                }
            } else {
                this.streak = 1;
            }
            this.lastChar = char;
        }
        if (this.streak === 3 && !this.firstTriplet) {
            this.firstTriplet = this.lastChar;
        } else if (this.streak === 5) {
            this.quintets.add(this.lastChar);
        }
        return [this.firstTriplet, this.quintets];
    }
}
