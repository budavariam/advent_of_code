import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["10000"], expected: "01100"},
];

checkResult(solution, data, {diskSize: 20});
