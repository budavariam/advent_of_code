import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "rotate based on position of letter d",
    ], expected: "cabde"},
    // I tested my inputs with the first solution, and logged out the steps in reverse, then diffed the outputs.
];

checkResult(solution, data, { seed: "decab"});
