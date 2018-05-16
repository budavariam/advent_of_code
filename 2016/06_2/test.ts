import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "abc",
        "abd",
        "efd"
    ],
    expected: "efc"},
];

checkResult(solution, data);
