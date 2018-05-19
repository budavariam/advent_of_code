export function solution(input: string[]) {
    const compressor = new Compressor();
    compressor.decompress(input[0]);
    return "" + compressor.extractedChars;
}

const enum State {
    READ_MARKER,
    CHARACTERS,
}

class Compressor {
    public extractedChars = 0;

    private state = State.CHARACTERS;
    private lastMarker = "";

    public decompress(line: string) {
        let result: string = "";
        for (let i = 0; i < line.length; i++) {
            const character = line[i];
            if (character === "(") {
                this.readMarker();
            } else if (character === ")") {
                this.readChar();
                const [slice, times] = this.processMarker(line, i + 1, this.lastMarker);
                result += this.applyMarker(slice, times);
                i += slice.length;
            } else if (this.state === State.READ_MARKER) {
                this.lastMarker += character;
            } else if (this.state === State.CHARACTERS) {
                result += character;
            }
        }
        this.extractedChars = result.length;
        // console.log(result.length, result);
        return result;
    }

    private readMarker() {
        this.lastMarker = "";
        this.state = State.READ_MARKER;
    }

    private readChar() {
        this.state = State.CHARACTERS;
    }

    private processMarker(line: string, index: number, marker: string): [string, number] {
        const instructions = marker.match(/(\d+)x(\d+)/);
        if (instructions) {
            const charNum = parseInt(instructions[1], 10);
            const times = parseInt(instructions[2], 10);
            const slice = line.slice(index, index + charNum);
            return [slice, times];
        } else {
            console.error("Error in instruction format: ", marker);
        }
        return ["", 0];
    }

    private applyMarker(slice: string, times: number) {
        let result: string = "";
        for (let i = 0; i < times; i++) {
            result += slice;
        }
        return result;
    }
}
