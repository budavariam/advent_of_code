export function solution(input: string[], options?: any) {
    const handler = new ChipHandler();
    handler.loadData(input);
    return "" + handler.multiplyOutputs(options.outputIDs);
}

/**
 * Flyweight to store the bots and outputs.
 */
class BotStore {
    private bots: {[botID: string]: Bot} = {};

    public getBot(botID: string): Bot {
        let bot;
        if (botID in this.bots) {
            bot = this.bots[botID];
        } else {
            bot = new Bot(botID);
            this.bots[botID] = bot;
        }
        return bot;
    }

    public getBotByChips(orderedChips: number[]): Bot | null {
        for (const botID in this.bots) {
            if (this.bots.hasOwnProperty(botID)) {
                const bot = this.bots[botID];
                if (bot.compareChips(orderedChips)) {
                    return bot;
                }
            }
        }
        return null;
    }
}

class ChipHandler {

    private bots: BotStore = new BotStore();

    public loadData(input: string[]) {
        input.forEach((line) => {
            const botData = line.match(/(bot \d+) gives low to ((?:bot|output) \d+) and high to ((?:bot|output) \d+)/);
            const initChip = botData ? null : line.match(/value (\d+) goes to (bot \d+)/);
            if (botData) {
                const botID = botData[1];
                const lowConnect = botData[2];
                const highConnect = botData[3];
                this.setBot(botID, lowConnect, highConnect);
            } else if (initChip) {
                const chipValue = parseInt(initChip[1], 10);
                const handlerBot = initChip[2];
                this.initChip(handlerBot, chipValue);
            } else {
                console.error("Parse error on line:", line);
            }
        });
    }

    public getBotByChips(chipLow: number, chipHigh: number): number {
        const chips = [chipLow, chipHigh];
        const bot = this.bots.getBotByChips(chips);
        return bot ? bot.getID() : -1;
    }

    public multiplyOutputs(outputIds: number[]) {
        return outputIds
            .map((i) => this.bots.getBot(`output ${i}`).getFirstChip())
            .reduce((acc, value) => acc *= value, 1);
    }

    private setBot(botID: string, lowConnect: string, highConnect: string) {
        this.bots.getBot(botID).setConnections(this.bots.getBot(lowConnect), this.bots.getBot(highConnect));
    }

    private initChip(botID: string, chipValue: number) {
        this.bots.getBot(botID).setChip(chipValue);
    }
}

class Bot {
    private sent = false;

    constructor(
        private name: string,
        private lowConnect?: Bot,
        private highConnect?: Bot,
        private chips: number[] = [],
    ) {}

    public setConnections(low: Bot, high: Bot) {
        this.lowConnect = low;
        this.highConnect = high;
        this.sendChips();
    }

    public setChip(value: number) {
        this.chips.push(value);
        this.sendChips();
    }

    public getID(): number {
        return parseInt(this.name.split(" ")[1], 10);
    }

    public compareChips(sortedChips: number[]): boolean {
        const [low, high] = sortedChips;
        return low === this.chips[0] && high === this.chips[1];
    }

    public getFirstChip(): number {
        return this.chips[0];
    }

    private sendChips() {
        if (!this.sent && this.lowConnect && this.highConnect && this.chips.length === 2) {
            const [lowChip, highChip] = this.chips.sort((a, b) => (a === b) ? 0 : (a > b ? 1 : -1));
            // console.log(this.name, "setChips", lowChip, highChip);
            this.lowConnect.setChip(lowChip);
            this.highConnect.setChip(highChip);
            this.sent = true;
        }
    }
}
