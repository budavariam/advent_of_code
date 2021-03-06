import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["R2, L3"], expected: "5"},
    {input: ["R2, R2, R2"], expected: "2"},
    {input: ["R5, L5, R5, R3"], expected: "12"},
];

checkResult(solution, data);
