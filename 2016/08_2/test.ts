import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1",
    ], expected: ""},
    {input: [
        "rect 1x2",
        "rect 2x2",
        "rect 3x2",
        "rect 3x4",
        "rect 1x5",
    ], expected: ""},
];

checkResult(solution, data);
