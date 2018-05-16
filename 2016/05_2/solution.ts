import { MD5 } from "crypto-js";

export function solution(input: string[]) {
    const passKey = new PassKey(input[0]);
    return passKey.getSecondDoorPassword();
}

class PassKey {
    private counter = 0;
    private password = new Array<string>(8);
    private gotChar = 0;

    constructor(private input: string) {}

    public getSecondDoorPassword(){
        while (this.gotChar < 8) {
            let hash = "";
            do {
                hash = MD5(this.input + this.counter++).toString();
            } while (!hash.match(/^00000/))
            const position = parseInt(hash.charAt(6 - 1), 10);
            //console.log(hash, this.counter, hash.charAt(5), hash.charAt(6), !isNaN(position), position <=7, !this.password[position]);
            if ( !isNaN(position) && position <=7 && !this.password[position]){
                const charToPut =  hash.charAt(7 - 1);
                this.password[position] = charToPut;
                this.gotChar++;
                //console.log(this.password);
            }
        }
        return this.password.join("");
    }
}