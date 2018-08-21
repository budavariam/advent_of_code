import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "swap position 4 with position 0",
        "swap letter d with letter b swaps",
        "reverse positions 0 through 4",
        "rotate left 1 step",
        "move position 1 to position 4",
        "move position 3 to position 0",
        "rotate based on position of letter b",
        "rotate based on position of letter d",
    ], expected: "decab"},
];

checkResult(solution, data, { seed: "abcde"});
