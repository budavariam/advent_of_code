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
            let maxIndex = -1;
            let maxElem = '-';
            for (let elem in posHistogram){
                if (posHistogram[elem] > maxIndex) {
                    maxElem = elem;
                    maxIndex = posHistogram[elem];
                }
            }
            return maxElem;
        }).join("");
    }
}