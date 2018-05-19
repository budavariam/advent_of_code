import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1",
    ], expected: "6"},
    {input: [
        "rect 1x2",
        "rect 2x2",
        "rect 3x2",
        "rect 3x4",
        "rect 1x5",
    ], expected: "13"},
];

checkResult(solution, data);
