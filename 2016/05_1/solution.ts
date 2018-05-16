import { MD5 } from "crypto-js";

export function solution(input: string[]) {
    const passKey = new PassKey(input[0]);
    return [0,1,2,3,4,5,6,7].map((_) => passKey.getNextChar()).join("");
}

class PassKey {
    private counter = 0;

    constructor(private input: string) {}

    public getNextChar(){
        let hash = "";
        do {
            hash = MD5(this.input + this.counter++).toString();
        } while (!hash.match(/^00000/))
        // console.log(hash, this.counter);
        return hash.charAt(6 - 1);
    }
}