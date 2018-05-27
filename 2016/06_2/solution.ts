export function solution(input: string[]) {
    const message = new Message(input);
    return message.getFilteredMessage();
}

type HistogramType = Array<{[charCount: string]: number}>;

class Message {
    private histogram: HistogramType = [];

    constructor(input: string[]) {
        for (const line of input) {
            line.split("").forEach((char, index) => {
                if (!this.histogram[index]) {
                    this.histogram[index] = {};
                }

                if (this.histogram[index][char]) {
                    this.histogram[index][char]++;
                } else {
                    this.histogram[index][char] = 1;
                }
            });
        }
    }

    public getFilteredMessage() {
        return this.histogram.map((posHistogram) => {
            let minIndex = Number.MAX_VALUE;
            let minElem = "-";
            for (const elem in posHistogram) {
                if (posHistogram[elem] < minIndex) {
                    minElem = elem;
                    minIndex = posHistogram[elem];
                }
            }
            return minElem;
        }).join("");
    }
}
