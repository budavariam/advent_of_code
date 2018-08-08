import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: ["ihgpwlah"], expected: "DDRRRD"},
    {input: ["kglvqrro"], expected: "DDUDRLRRUDRD"},
    {input: ["ulqzkmiv"], expected: "DRURDRUDDLLDLUURRDULRLDUUDDDRR"},
];

checkResult(solution, data);
