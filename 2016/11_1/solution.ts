
export function solution(input: string[], options?: any) {
    const optimizer = new Optimizer(input);
    return "" + optimizer.shortestPath();
}

class Optimizer {
    private queue: State[] = [];
    private visited: Set<string> = new Set<string>();
    private floorCount = 0;

    constructor(input: string[]) {
        const items = /(\w+(?:-compatible microchip| generator))/g;
        const parsed: {generator: Map<string, number>, microchip: Map<string, number>} = {
            generator: new Map<string, number>(),
            microchip: new Map<string, number>(),
        };
        input.forEach((line, floorNumber) => ((line.match(items) || []))
            .map((name) => {
                const tokens = name.split(" ");
                const material = tokens[0].split("-")[0][0].toUpperCase();
                const type = tokens[1] as "microchip"|"generator";
                parsed[type].set(material, floorNumber);
            }));
        const state = new State(parsed.generator, parsed.microchip);
        this.queue.push(state);
        this.visited.add(state.hash());
        this.floorCount = input.length - 1;
    }

    public shortestPath() {
        while (this.queue.length > 0) {
            const state = this.queue.shift();
            if (state) {
                // console.log(state.level); //state.hash());
                // state.print(this.floorCount);
                this.queue = this.queue.concat(state.getNextValidStates(this.floorCount, this.visited));
                if (state.isFinished(this.floorCount)) {
                    return state.level;
                }
            } else {
                console.error("No more elements, but the loop did not end somehow.");
            }
        }
        return 0;
    }
}

class State {
    public static clone(state: State): State {
        // Object.assign(Object.create(Object.getPrototypeOf(state)), state);
        return new State(new Map(state.generator), new Map(state.microchip), state.elevator, state.level, state);
    }

    constructor(
        public generator: Map<string, number>,
        public microchip: Map<string, number>,
        public elevator: number = 0,
        public level: number = 0,
        public parent?: State,
    ) {}

    public isFinished(endState: number) {
        const items = [...Array.from(this.generator), ...Array.from(this.microchip)];
        return !items.some(([key, value]) => value !== endState );
    }

    public isSafe(): boolean {
        // if a chip is ever left in the same area as another RTG,
        // and it's not connected to its own RTG, the chip will be fried
        const generators = Array.from(this.generator);
        const microchips = Array.from(this.microchip);
        return !microchips
            .some(([chipName, chipFloor]) => chipFloor !== (this.generator.get(chipName) || -1) &&
                generators.some(([genName, genFloor]) => genName !== chipName && chipFloor === genFloor));
    }

    public print(maxFloor: number) {
        const matrix: string[][] = [];
        for (let floor = 0; floor <= maxFloor; floor++) {
            matrix[floor] = [this.elevator === maxFloor - floor ? "E " : ". "];
        }
        for (const [elemName, elemFloor] of Array.from(this.generator)) {
            for (let floor = 0; floor <= maxFloor; floor++) {
                matrix[floor].push(elemFloor === maxFloor - floor ? elemName + "G" : ". ");
                const chipFloor = (this.microchip.get(elemName) || 0);
                matrix[floor].push(chipFloor === maxFloor - floor ? elemName + "M" : ". ");
            }
        }
        matrix.forEach((line, index) => console.log(`F${maxFloor - index} ${line.join(" ")}`));
        console.log();
    }

    public hash() {
        const hashObj = {
            e: this.elevator,
            g: Array.from(this.generator),
            m: Array.from(this.microchip),
        };
        return JSON.stringify(hashObj);
    }

    public getNextValidStates(maxFloor: number, visited: Set<string>): State[] {
        // do not move down other then the elevator
        // do not move into dangerous state
        // do not not move into visited state
        // do not step outside the floors
        return [
            ...this.moveOneElement(maxFloor, visited, 1),
            ...this.moveOneElement(maxFloor, visited, -1),
            ...this.moveUpTwoElements(maxFloor, visited),
        ];
    }

    private moveOnefromAll(
            maxFloor: number,
            visited: Set<string>,
            direction: number = 1,
            type: "generator"|"microchip",
        ) {
        const result: State[] = [];
        for (const [key, value] of Array.from(this[type].entries())) {
            if (this.elevator === value) {
                const newState = State.clone(this);
                newState.level = this.level + 1;
                newState[type].set(key, value + direction);
                newState.elevator += direction;
                const hash = newState.hash();
                if (!visited.has(hash)) {
                    visited.add(hash);
                    if (newState.isSafe()) {
                        result.push(newState);
                    }
                }
            }
        }
        return result;
    }

    private moveDuelUp(
        maxFloor: number,
        visited: Set<string>,
        firstName: string,
        firstType: "generator"|"microchip",
        secondName: string,
        secondType: "generator"|"microchip",
    ) {
    const newState = State.clone(this);
    newState.level = this.level + 1;
    newState[firstType].set(firstName, (newState[firstType].get(firstName) || 0) + 1);
    newState[secondType].set(secondName, (newState[secondType].get(secondName) || 0) + 1);
    newState.elevator += 1;
    const hash = newState.hash();
    if (!visited.has(hash)) {
        visited.add(hash);
        if (newState.isSafe()) {
            return newState;
        }
    }
    return null;
}

    private moveOneElement(maxFloor: number, visited: Set<string>, direction: number = 1): State[] {
        let result: State[] = [];
        if ((this.elevator !== maxFloor && direction > 0) || (this.elevator > 0 && direction < 0)) {
            result = result.concat(this.moveOnefromAll(maxFloor, visited, direction, "generator"));
            result = result.concat(this.moveOnefromAll(maxFloor, visited, direction, "microchip"));
        }
        return result;
    }

    private moveUpTwoElements(maxFloor: number, visited: Set<string>): State[] {
        const result: State[] = [];
        if (this.elevator !== maxFloor) {
            const sameFloorItems = [
                ...Array.from(this.microchip)
                    .filter(([chipName, chipFloor]) => chipFloor === this.elevator)
                    .map((elem: [string, number]) => [elem[0], "microchip"]),
                ...Array.from(this.generator)
                    .filter(([genName, genFloor]) => genFloor === this.elevator)
                    .map((elem: [string, number]) => [elem[0], "generator"]),
                ] as [string, "microchip"|"generator"][];
            const combinationIDs = COMBINATIONS.generateDualCombinations(sameFloorItems.length);
            for (const [first, second] of combinationIDs) {
                const [firstName, firstType] = sameFloorItems[first];
                const [secondName, secondType] = sameFloorItems[second];
                const newState = this.moveDuelUp(maxFloor, visited, firstName, firstType, secondName, secondType);
                if (newState) {
                    result.push(newState);
                }
            }
        }
        return result;
    }
}

class Combinations {
    public combinationCache = new Map<number, Array<[number, number]>>();

    public generateDualCombinations(numberCount: number): Array<[number, number]> {
        const result: Array<[number, number]> = [];
        const hasCached = this.combinationCache.get(numberCount);
        if (hasCached) {
            return hasCached;
        } else {
            for (let i = 0; i < numberCount; i++) {
                for (let j = 0; j < numberCount; j++) {
                    if (i !== j ) {
                        result.push([i, j]);
                    }
                }
            }
            this.combinationCache.set(numberCount, result);
        }
        return result;
    }
}

const COMBINATIONS = new Combinations();
