export function solution(input: string[]): string {
    const triangles: string[] = input
        .filter((rawInput: string) => {
            const sides: number[] = rawInput
                .trim()
                .split(/\s+/)
                .map((rawNumber) => parseInt(rawNumber, 10));
            return isValidTriangle(sides);
        });
    return "" + triangles.length;
}

function isValidTriangle(sides: number[]) {
    return [0, 1, 2].every((i: number) => sides[i] < sides[(i + 1) % 3] + sides[(i + 2) % 3]);
}
