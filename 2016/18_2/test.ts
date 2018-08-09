import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["..^^."], expected: "16"},
    {input: [".^^.^.^^^^"], expected: "38"},
];

checkResult(solution, data, {count: 10});
