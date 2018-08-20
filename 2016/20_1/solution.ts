export function solution(input: string[], options?: any) {
    const list = input.map((line) => line.split("-").map((elem) => parseInt(elem, 10))).sort((a, b) => a[0] - b[0]);
    let candidate = null;
    for (const [a, b] of list) {
        if (candidate === null || candidate <= b && candidate >= a) {
            candidate = b + 1;
        }
    }
    return "" + candidate;
}
