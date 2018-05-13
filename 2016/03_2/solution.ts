export function solution(input: string[]): string {
    const inputLength = input.length;
    const nums = input.map((line) => line.trim().split(/\s+/).map((rawNumber) => parseInt(rawNumber, 10)));

    let result = 0;
    for (let step = 0; step < inputLength; step += 3) {
        result += [0, 1, 2].filter((rowCount) => isValidTriangle([
                nums[step + 0][rowCount],
                nums[step + 1][rowCount],
                nums[step + 2][rowCount],
                ]),
            ).length;
    }
    return "" + result;
}

function isValidTriangle(sides: number[]) {
    return [0, 1, 2].every((i: number) => sides[i] < sides[(i + 1) % 3] + sides[(i + 2) % 3]);
}
