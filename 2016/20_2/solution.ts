export function solution(input: string[], options?: any) {
    const list = input.map((line) => line.split("-").map((elem) => parseInt(elem, 10))).sort((a, b) => a[0] - b[0]);
    let [current, total, index] = [0, 0, 0];
    const maxIndex = list.length;
    while (current < options.max ) {
        if (index >= maxIndex) {
            total += options.max - (current - 1);
            break;
        }
        const [a, b] = list[index];
        if (current >= a) {
            if (current <= b) {
                current = b + 1;
            }
            index++;
        } else {
            total += (a - current);
            current = a;
        }
    }
    return "" + total;
}
