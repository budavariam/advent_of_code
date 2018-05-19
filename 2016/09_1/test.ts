import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["ADVENT"], expected: "6"},
    {input: ["A(1x5)BC"], expected: "7"},
    {input: ["(3x3)XYZ"], expected: "9"},
    {input: ["A(2x2)BCD(2x2)EFG"], expected: "11"},
    {input: ["(6x1)(1x3)A"], expected: "6"},
    {input: ["X(8x2)(3x3)ABCY"], expected: "18"},
];

checkResult(solution, data);
