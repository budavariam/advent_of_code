import { TLSSocket } from "tls";

export function solution(input: string[]) {
    return "" + input
        .map((line) => new IPv7(line))
        .filter((ip) => ip.supportsTLS)
        .length;
}

const isEven = (_: any, index: number) => index % 2 === 1;
const isOdd =  (_: any, index: number) => index % 2 === 0;

class IPv7 {
    private checkABBA(input: string) {
        for (let i = 3; i < input.length; i++) {
            if (input[i] === input[i-3] && input[i] !== input[i-2] && input[i-2] === input[i-1]) {
                return true;
            }
        }
        return false;
    }

    constructor(private line: string) {
        const parts = line.split(/\[|\]/); // odd index: bracketed; even: outside
        
        const inBrackets = parts
            .filter(isEven)
            .some(this.checkABBA);
        const outsideBrackets = parts
            .filter(isOdd)
            .some(this.checkABBA);
        
        this.supportsTLS = !inBrackets && outsideBrackets;
    }

    public supportsTLS = false;
}