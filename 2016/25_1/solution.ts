export function solution(input: string[], options?: any) {
    /**
     * I've written down the code of the input, and figured out that it prints the binary representation of the number.
     *
     * The first part adds a constant to the initial value.
     * The second part calculates the binary representation of the code, by halving the value and getting mod 2;
     * If it reaches zero it starts again, printing the values in an infinite loop.
     *
     * So I should find the next number from the given constant, that has an alternating binary pattern,
     * and the solution will be the difference between them.
     */
    const c = parseInt(input[1].split(" ")[1], 10);
    const b = parseInt(input[2].split(" ")[1], 10);
    const multiplied = c * b;
    const result = findFirstBiggerAlternatingBitpattern(multiplied) - multiplied;
    return "" + result;
}

function findFirstBiggerAlternatingBitpattern(lowerbound: number) {
    let current = 0;
    let i = 0;
    while (current < lowerbound) {
        i = (i + 1) % 2;
        current <<= 1;
        current |= i;
        // console.log((current >>> 0).toString(2));
    }
    return current;
}
