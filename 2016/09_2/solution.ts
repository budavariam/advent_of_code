export function solution(input: string[]) {
    const compressor = new Compressor();
    return "" + compressor.decompress(input[0]);
}

const enum State {
    READ_MARKER,
    CHARACTERS,
}

class Compressor {
    public decompress(line: string) {
        let result = 0;
        let state = State.CHARACTERS;
        let lastMarker = "";
        for (let i = 0; i < line.length; i++) {
            const character = line[i];
            if (character === "(") {
                lastMarker = "";
                state = State.READ_MARKER;
            } else if (character === ")") {
                state = State.CHARACTERS;
                const [sliceLength, decomressedLength] = this.processMarker(line, i + 1, lastMarker);
                result += decomressedLength;
                i += sliceLength;
            } else if (state === State.READ_MARKER) {
                lastMarker += character;
            } else if (state === State.CHARACTERS) {
                result += 1;
            }
        }
        return result;
    }

    private processMarker(line: string, index: number, marker: string): [number, number] {
        const instructions = marker.match(/(\d+)x(\d+)/);
        if (instructions) {
            const charNum = parseInt(instructions[1], 10);
            const times = parseInt(instructions[2], 10);
            const slice = line.slice(index, index + charNum);
            const decompressedInside = this.decompress(slice);
            return [slice.length, (decompressedInside) * times];
        } else {
            console.error("Error in instruction format: ", marker);
        }
        return [0, 0];
    }
}
