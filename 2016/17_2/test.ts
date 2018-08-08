import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["ihgpwlah"], expected: "370"},
    {input: ["kglvqrro"], expected: "492"},
    {input: ["ulqzkmiv"], expected: "830"},
];

checkResult(solution, data);
