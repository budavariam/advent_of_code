export function solution(input: string[]) {
    const message = new Message(input);
    return message.getFilteredMessage();
}

type HistogramType = {[charCount: string]: number}[];

class Message {
    private histogram: HistogramType = [];

    constructor(private input: string[]) {
        for (let line of input) {
            line.split("").forEach((char, index) => {
                if (!this.histogram[index]){
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

    public getFilteredMessage(){
        return this.histogram.map((posHistogram) => {
            let minIndex = Number.MAX_VALUE;
            let minElem = '-';
            for (let elem in posHistogram){
                if (posHistogram[elem] < minIndex) {
                    minElem = elem;
                    minIndex = posHistogram[elem];
                }
            }
            return minElem;
        }).join("");
    }
}