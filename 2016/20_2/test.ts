import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["5-8", "0-2", "4-7"], expected: "3"},
];

checkResult(solution, data, {max: 10});
