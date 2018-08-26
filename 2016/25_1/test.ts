import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "cpy a d",
        "cpy 4 c",
        "cpy 633 b",
    ], expected: "198"},
];

checkResult(solution, data);
